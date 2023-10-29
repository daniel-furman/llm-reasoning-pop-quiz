# custom text generation function
# requires "model" and "tokenizer" global vars initiated above

from typing import List
import transformers
import torch
import warnings

# supress warnings
warnings.filterwarnings("ignore")

# set the device
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")


class llm_boiler:
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
        self.model, self.tokenizer = self.load_fn(self.model_id)
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
    temperature: float = 0.7,
    top_p: float = 0.95,
    top_k: int = 50,
    num_return_sequences: int = 1,
    debug: bool = False,
) -> str:
    # streamer = transformers.TextStreamer(tokenizer)

    # We use the tokenizer's chat template to format each message - see https://huggingface.co/docs/transformers/main/en/chat_templating
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


LOAD_MODEL_FUNCTIONS.append(mistral_loader)


def mistral(
    model: transformers.AutoModelForCausalLM,
    tokenizer: transformers.AutoTokenizer,
    prompt: str,
    eos_token_ids: List[int],
    max_new_tokens: int = 128,
    do_sample: bool = True,
    temperature: int = 1.0,
    top_p: int = 1.0,
    top_k: int = 50,
    num_return_sequences: int = 1,
) -> str:
    streamer = transformers.TextStreamer(tokenizer)

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
        num_return_sequences=num_return_sequences,
        pad_token_id=tokenizer.eos_token_id,
        bos_token_id=tokenizer.eos_token_id,
        streamer=streamer,
    )

    if num_return_sequences == 1:
        generated_text = tokenizer.decode(
            output_tokens[0][len(inputs.input_ids[0]) :], skip_special_tokens=True
        )
        if generated_text[0] == " ":
            generated_text = generated_text[1:]

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

        return generated_text_list


MODEL_FUNCTIONS.append(mistral)


## llama-2 models
def llama_loader(
    model_id: str,  # HF model id
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
        use_auth_token=True,
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
    temperature: float = 0.7,
    top_p: float = 0.95,
    top_k: int = 50,
    num_return_sequences: int = 1,
    debug: bool = False,
) -> str:
    # streamer = transformers.TextStreamer(tokenizer)

    # We use the tokenizer's chat template to format each message - see https://huggingface.co/docs/transformers/main/en/chat_templating
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


## falcon models
def falcon_loader(
    model_id: str,  # HF model id
):
    # see source: https://huggingface.co/tiiuae/falcon-40b-instruct#how-to-get-started-with-the-model
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
        trust_remote_code=True,
    )

    return model, tokenizer


LOAD_MODEL_FUNCTIONS.append(falcon_loader)


def falcon(
    model: transformers.AutoModelForCausalLM,
    tokenizer: transformers.AutoTokenizer,
    prompt: str,
    eos_token_ids: List[int],
    max_new_tokens: int = 128,
    do_sample: bool = True,
    temperature: int = 1.0,
    top_p: int = 1.0,
    top_k: int = 50,
    num_return_sequences: int = 1,
) -> str:
    streamer = transformers.TextStreamer(tokenizer)

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
        num_return_sequences=num_return_sequences,
        pad_token_id=tokenizer.eos_token_id,
        bos_token_id=tokenizer.eos_token_id,
        streamer=streamer,
    )

    if num_return_sequences == 1:
        generated_text = tokenizer.decode(
            output_tokens[0][len(inputs.input_ids[0]) :], skip_special_tokens=True
        )
        if generated_text[0] == " ":
            generated_text = generated_text[1:]

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

        return generated_text_list


MODEL_FUNCTIONS.append(falcon)


## flan models
def flan_loader(
    model_id: str,  # HF model id
):
    # see source: https://huggingface.co/google/flan-t5-xxl#fp16
    tokenizer = transformers.T5Tokenizer.from_pretrained(model_id)

    model = transformers.T5ForConditionalGeneration.from_pretrained(
        model_id, device_map="auto", torch_dtype=torch.float16
    )

    return model, tokenizer


LOAD_MODEL_FUNCTIONS.append(flan_loader)


def flan(
    model: transformers.AutoModelForCausalLM,
    tokenizer: transformers.AutoTokenizer,
    prompt: str,
    eos_token_ids: List[int],
    max_new_tokens: int = 128,
    do_sample: bool = True,
    temperature: int = 1.0,
    top_p: int = 1.0,
    top_k: int = 50,
    num_return_sequences: int = 1,
) -> str:
    streamer = transformers.TextStreamer(tokenizer)

    inputs = tokenizer(
        prompt,
        padding=True,
        truncation=True,
        return_tensors="pt",
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
        num_return_sequences=num_return_sequences,
        pad_token_id=tokenizer.eos_token_id,
        bos_token_id=tokenizer.eos_token_id,
        streamer=streamer,
    )

    if num_return_sequences == 1:
        generated_text = tokenizer.decode(output_tokens[0], skip_special_tokens=True)
        return generated_text

    else:
        generated_text_list = []
        for i in range(num_return_sequences):
            generated_text = tokenizer.decode(
                output_tokens[i],
                skip_special_tokens=True,
            )
            generated_text_list.append(generated_text)

        return generated_text_list


MODEL_FUNCTIONS.append(flan)


## mpt models
def mpt_loader(
    model_id: str,  # HF model id
):
    # see source: https://huggingface.co/tiiuae/mpt-40b-instruct#how-to-get-started-with-the-model
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
        trust_remote_code=True,
    )

    return model, tokenizer


LOAD_MODEL_FUNCTIONS.append(mpt_loader)


def mpt(
    model: transformers.AutoModelForCausalLM,
    tokenizer: transformers.AutoTokenizer,
    prompt: str,
    eos_token_ids: List[int],
    max_new_tokens: int = 128,
    do_sample: bool = True,
    temperature: int = 1.0,
    top_p: int = 1.0,
    top_k: int = 50,
    num_return_sequences: int = 1,
) -> str:
    streamer = transformers.TextStreamer(tokenizer)

    def format_prompt(instruction):
        template = "Below is an instruction that describes a task. Write a response that appropriately completes the request.\n\n###Instruction\n{instruction}\n\n### Response\n"
        return template.format(instruction=instruction)

    prompt = format_prompt(instruction=prompt)

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
        num_return_sequences=num_return_sequences,
        pad_token_id=tokenizer.eos_token_id,
        bos_token_id=tokenizer.eos_token_id,
        streamer=streamer,
    )

    if num_return_sequences == 1:
        generated_text = tokenizer.decode(
            output_tokens[0][len(inputs.input_ids[0]) :], skip_special_tokens=True
        )
        if generated_text[0] == " ":
            generated_text = generated_text[1:]

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

        return generated_text_list


MODEL_FUNCTIONS.append(mpt)
