# custom text generation functions for transformers and openai

from typing import List
import warnings
from dotenv import load_dotenv
import os

import transformers
#from peft import PeftModel, PeftConfig
import torch
import openai


# supress warnings
warnings.filterwarnings("ignore")

# set the device
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")


class hf_llm_boiler:
    def __init__(self, model_id, peft):
        self.model_id = model_id
        self.peft = peft
        for f_idx, run_function in enumerate(MODEL_FUNCTIONS):
            if run_function.__name__.lower() in self.model_id.lower():
                print(
                    f"Load function recognized for {self.model_id}: {LOAD_MODEL_FUNCTIONS[f_idx].__name__}"
                )
                self.load_fn = LOAD_MODEL_FUNCTIONS[f_idx]
        for run_function in MODEL_FUNCTIONS:
            if run_function.__name__.lower() in self.model_id.lower():
                print(
                    f"Run function recognized for {self.model_id}: {run_function.__name__.lower()}"
                )
                self.run_fn = run_function
        self.model, self.tokenizer = self.load_fn(self.model_id, self.peft)
        self.name = self.run_fn.__name__.lower()

    def run(
        self,
        prompt,
        eos_token_ids,
        max_new_tokens,
        temperature,
        do_sample,
        top_p,
        top_k,
        repetition_penalty,
        num_return_sequences,
        debug,
    ):
        return self.run_fn(
            model=self.model,
            tokenizer=self.tokenizer,
            prompt=prompt,
            eos_token_ids=eos_token_ids,
            max_new_tokens=max_new_tokens,
            temperature=temperature,
            do_sample=do_sample,
            top_p=top_p,
            top_k=top_k,
            repetition_penalty=repetition_penalty,
            num_return_sequences=num_return_sequences,
            debug=debug,
        )


LOAD_MODEL_FUNCTIONS = []
MODEL_FUNCTIONS = []

# Models must have
# * loader and generate functions
# * run function must identify the correct model_id
# * all functions must be added to master lists in order


## zephyr models
def zephyr_loader(
    model_id: str,  # HF model id
    peft: bool,  # Whether model is a peft adapter
):
    tokenizer = transformers.AutoTokenizer.from_pretrained(model_id)
    tokenizer.pad_token = tokenizer.eos_token

    bnb_config = transformers.BitsAndBytesConfig(
        load_in_4bit=True,
        bnb_4bit_use_double_quant=True,
        bnb_4bit_quant_type="nf4",
        bnb_4bit_compute_dtype=torch.bfloat16,
    )

    model = transformers.AutoModelForCausalLM.from_pretrained(
        model_id,
        quantization_config=bnb_config,
        device_map={"": 0},
    )

    return model, tokenizer


LOAD_MODEL_FUNCTIONS.append(zephyr_loader)


def zephyr(
    model: transformers.AutoModelForCausalLM,
    tokenizer: transformers.AutoTokenizer,
    prompt: str,
    eos_token_ids: List[int],
    max_new_tokens: int = 128,
    do_sample: bool = True,
    temperature: float = 0.1,
    top_p: float = 0.95,
    top_k: int = 50,
    repetition_penalty: float = 1.0,
    num_return_sequences: int = 1,
    debug: bool = False,
) -> str:
    # streamer = transformers.TextStreamer(tokenizer)

    messages = [
        {"role": "user", "content": prompt},
    ]
    prompt = tokenizer.apply_chat_template(
        messages, tokenize=False, add_generation_prompt=True
    )
    if debug:
        print(f"*** Prompt\n{prompt}")

    inputs = tokenizer(
        prompt,
        padding=True,
        truncation=True,
        return_tensors="pt",
        return_token_type_ids=False,
    )
    inputs = inputs.to(device)

    output_tokens = model.generate(
        **inputs,
        eos_token_id=eos_token_ids,
        max_new_tokens=max_new_tokens,
        do_sample=do_sample,
        temperature=temperature,
        top_p=top_p,
        top_k=top_k,
        repetition_penalty=repetition_penalty,
        num_return_sequences=num_return_sequences,
        pad_token_id=tokenizer.eos_token_id,
        bos_token_id=tokenizer.eos_token_id,
        # streamer=streamer,
    )

    if num_return_sequences == 1:
        generated_text = tokenizer.decode(
            output_tokens[0][len(inputs.input_ids[0]) :], skip_special_tokens=True
        )
        if generated_text[0] == " ":
            generated_text = generated_text[1:]

        if debug:
            print(f"*** Generated\n{generated_text}")

        return generated_text

    else:
        generated_text_list = []
        for i in range(num_return_sequences):
            generated_text = tokenizer.decode(
                output_tokens[i][len(inputs.input_ids[0]) :],
                skip_special_tokens=True,
            )
            if generated_text[0] == " ":
                generated_text = generated_text[1:]
            generated_text_list.append(generated_text)
        if debug:
            print(f"*** Generated\n{str(generated_text_list)}")

        return generated_text_list


MODEL_FUNCTIONS.append(zephyr)


## mistral models
def mistral_loader(
    model_id: str,  # HF model id
    peft: bool,  # Whether model is a peft adapter
):
    config = PeftConfig.from_pretrained(model_id)
    tokenizer = transformers.AutoTokenizer.from_pretrained(model_id)
    tokenizer.pad_token = tokenizer.eos_token

    # bnb_config = transformers.BitsAndBytesConfig(
    #    load_in_4bit=True,
    #    bnb_4bit_use_double_quant=True,
    #    bnb_4bit_quant_type="nf4",
    #    bnb_4bit_compute_dtype=torch.bfloat16,
    # )

    if not peft:
        model = transformers.AutoModelForCausalLM.from_pretrained(
            model_id,
            torch_dtype=torch.float16,
            device_map="auto",
        )

    if peft:
        model = transformers.AutoModelForCausalLM.from_pretrained(
            config.base_model_name_or_path,
            torch_dtype=torch.float16,
            device_map="auto",
        )

        model = PeftModel.from_pretrained(model, model_id)

    return model, tokenizer


LOAD_MODEL_FUNCTIONS.append(mistral_loader)


def mistral(
    model: transformers.AutoModelForCausalLM,
    tokenizer: transformers.AutoTokenizer,
    prompt: str,
    eos_token_ids: List[int],
    max_new_tokens: int = 128,
    do_sample: bool = True,
    temperature: float = 0.1,
    top_p: float = 0.95,
    top_k: int = 50,
    repetition_penalty: float = 1.0,
    num_return_sequences: int = 1,
    debug: bool = False,
) -> str:
    # streamer = transformers.TextStreamer(tokenizer)

    messages = [
        {"role": "user", "content": prompt},
    ]
    prompt = tokenizer.apply_chat_template(
        messages, tokenize=False, add_generation_prompt=True
    )
    if debug:
        print(f"*** Prompt\n{prompt}")

    inputs = tokenizer(
        prompt,
        padding=True,
        truncation=True,
        return_tensors="pt",
        return_token_type_ids=False,
    )
    inputs = inputs.to(device)

    output_tokens = model.generate(
        **inputs,
        eos_token_id=eos_token_ids,
        max_new_tokens=max_new_tokens,
        do_sample=do_sample,
        temperature=temperature,
        top_p=top_p,
        top_k=top_k,
        repetition_penalty=repetition_penalty,
        num_return_sequences=num_return_sequences,
        pad_token_id=tokenizer.eos_token_id,
        bos_token_id=tokenizer.eos_token_id,
        # streamer=streamer,
    )

    if num_return_sequences == 1:
        generated_text = tokenizer.decode(
            output_tokens[0][len(inputs.input_ids[0]) :], skip_special_tokens=True
        )
        if generated_text[0] == " ":
            generated_text = generated_text[1:]

        if debug:
            print(f"*** Generated\n{generated_text}")

        return generated_text

    else:
        generated_text_list = []
        for i in range(num_return_sequences):
            generated_text = tokenizer.decode(
                output_tokens[i][len(inputs.input_ids[0]) :],
                skip_special_tokens=True,
            )
            if generated_text[0] == " ":
                generated_text = generated_text[1:]
            generated_text_list.append(generated_text)
        if debug:
            print(f"*** Generated\n{str(generated_text_list)}")

        return generated_text_list


MODEL_FUNCTIONS.append(mistral)


## llama models


def llama_loader(
    model_id: str,  # HF model id
    peft: bool,  # Whether model is a peft adapter
):
    tokenizer = transformers.AutoTokenizer.from_pretrained(model_id)
    tokenizer.pad_token = tokenizer.eos_token

    bnb_config = transformers.BitsAndBytesConfig(
        load_in_4bit=True,
        bnb_4bit_use_double_quant=True,
        bnb_4bit_quant_type="nf4",
        bnb_4bit_compute_dtype=torch.bfloat16,
    )

    model = transformers.AutoModelForCausalLM.from_pretrained(
        model_id,
        quantization_config=bnb_config,
        device_map={"": 0},
    )

    return model, tokenizer


LOAD_MODEL_FUNCTIONS.append(llama_loader)


def llama(
    model: transformers.AutoModelForCausalLM,
    tokenizer: transformers.AutoTokenizer,
    prompt: str,
    eos_token_ids: List[int],
    max_new_tokens: int = 128,
    do_sample: bool = True,
    temperature: float = 0.1,
    top_p: float = 0.95,
    top_k: int = 50,
    repetition_penalty: float = 1.0,
    num_return_sequences: int = 1,
    debug: bool = False,
) -> str:
    # streamer = transformers.TextStreamer(tokenizer)

    messages = [
        {"role": "system", "content": "Your are a helpful AI assistant."},
        {"role": "user", "content": prompt},
    ]
    prompt = tokenizer.apply_chat_template(
        messages, tokenize=False, add_generation_prompt=True
    )
    if debug:
        print(f"*** Prompt\n{prompt}")

    inputs = tokenizer(
        prompt,
        padding=True,
        truncation=True,
        return_tensors="pt",
        return_token_type_ids=False,
    )
    inputs = inputs.to(device)

    output_tokens = model.generate(
        **inputs,
        eos_token_id=eos_token_ids,
        max_new_tokens=max_new_tokens,
        do_sample=do_sample,
        temperature=temperature,
        top_p=top_p,
        top_k=top_k,
        repetition_penalty=repetition_penalty,
        num_return_sequences=num_return_sequences,
        pad_token_id=tokenizer.eos_token_id,
        bos_token_id=tokenizer.eos_token_id,
        # streamer=streamer,
    )

    if num_return_sequences == 1:
        generated_text = tokenizer.decode(
            output_tokens[0][len(inputs.input_ids[0]) :], skip_special_tokens=True
        )
        if generated_text[0] == " ":
            generated_text = generated_text[1:]

        if debug:
            print(f"*** Generated\n{generated_text}")

        return generated_text

    else:
        generated_text_list = []
        for i in range(num_return_sequences):
            generated_text = tokenizer.decode(
                output_tokens[i][len(inputs.input_ids[0]) :],
                skip_special_tokens=True,
            )
            if generated_text[0] == " ":
                generated_text = generated_text[1:]
            generated_text_list.append(generated_text)
        if debug:
            print(f"*** Generated\n{str(generated_text_list)}")

        return generated_text_list


MODEL_FUNCTIONS.append(llama)


class openai_llm_boiler:
    def __init__(self, model_id):
        self.model_id = model_id
        for f_idx, run_function in enumerate(MODEL_FUNCTIONS):
            if run_function.__name__.lower() in self.model_id:
                print(
                    f"Load function recognized for {self.model_id}: {LOAD_MODEL_FUNCTIONS[f_idx].__name__}"
                )
                self.load_fn = LOAD_MODEL_FUNCTIONS[f_idx]
        for run_function in MODEL_FUNCTIONS:
            if run_function.__name__.lower() in self.model_id:
                print(
                    f"Run function recognized for {self.model_id}: {run_function.__name__.lower()}"
                )
                self.run_fn = run_function
        self.client = self.load_fn()
        self.name = self.run_fn.__name__.lower()

    def run(
        self,
        prompt,
        temperature,
        debug,
    ):
        return self.run_fn(
            client=self.client,
            prompt=prompt,
            temperature=temperature,
            debug=debug,
        )


# Models must have
# * loader and generate functions
# * run function must identify the correct model_id
# * all functions must be added to master lists in order


## gpt-3.5-turbo model
def gpt_3_5_turbo_loader():
    load_dotenv()
    client = openai.OpenAI()
    return client


LOAD_MODEL_FUNCTIONS.append(gpt_3_5_turbo_loader)


def gpt_3_5_turbo(
    client,
    prompt: str,
    temperature: float = 0.1,
    debug: bool = False,
) -> str:
    if debug:
        print(f"*** Prompt\nYou are a helpful assistant. {prompt}")

    # example with a system message
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {
                "role": "user",
                "content": prompt,
            },
        ],
        temperature=temperature,
        seed=42,
    )

    generated_text = response.choices[0].message.content

    if debug:
        print(f"*** Generated\n{generated_text}")

    return generated_text


MODEL_FUNCTIONS.append(gpt_3_5_turbo)


## gpt-4 model
def gpt_4_loader():
    load_dotenv()
    client = openai.OpenAI()
    return client


LOAD_MODEL_FUNCTIONS.append(gpt_4_loader)


def gpt_4(
    client,
    prompt: str,
    temperature: float = 0.1,
    debug: bool = False,
) -> str:
    if debug:
        print(f"*** Prompt\nYou are a helpful assistant. {prompt}")

    # example with a system message
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {
                "role": "user",
                "content": prompt,
            },
        ],
        temperature=temperature,
        seed=42,
    )

    generated_text = response.choices[0].message.content

    if debug:
        print(f"*** Generated\n{generated_text}")

    return generated_text


MODEL_FUNCTIONS.append(gpt_4)
