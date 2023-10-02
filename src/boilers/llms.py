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
        )


LOAD_MODEL_FUNCTIONS = []
MODEL_FUNCTIONS = []

# Models must have
# * loader and generate functions
# * run function must identify the correct model_id
# * all functions must be added to master lists in order


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
    """
    Initialize the pipeline
    Uses Hugging Face GenerationConfig defaults
        https://huggingface.co/docs/transformers/v4.29.1/en/main_classes/text_generation#transformers.GenerationConfig
    Args:
        model (transformers.AutoModelForCausalLM): Falcon model for text generation
        tokenizer (transformers.AutoTokenizer): Tokenizer for model
        prompt (str): Prompt for text generation
        eos_token_ids (List[int]): the eos_token(s) for the text generation
        max_new_tokens (int, optional): Max new tokens after the prompt to generate. Defaults to 128.
        do_sample (bool, optional): Whether or not to use sampling. Defaults to True.
        temperature (float, optional): The value used to modulate the next token probabilities.
            Defaults to 1.0
        top_p (float, optional): If set to float < 1, only the smallest set of most probable tokens with
            probabilities that add up to top_p or higher are kept for generation. Defaults to 1.0.
        top_k (int, optional): The number of highest probability vocabulary tokens to keep for top-k-filtering.
            Defaults to 50.
        num_return_sequences (int, optional): The number of independently computed returned sequences for each
            element in the batch. Defaults to 1.
    """
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
    temperature: int = 1.0,
    top_p: int = 1.0,
    top_k: int = 50,
    num_return_sequences: int = 1,
) -> str:
    """
    Initialize the pipeline
    Uses Hugging Face GenerationConfig defaults
        https://huggingface.co/docs/transformers/v4.29.1/en/main_classes/text_generation#transformers.GenerationConfig
    Args:
        model (transformers.AutoModelForCausalLM): Falcon model for text generation
        tokenizer (transformers.AutoTokenizer): Tokenizer for model
        prompt (str): Prompt for text generation
        eos_token_ids (List[int]): the eos_token(s) for the text generation
        max_new_tokens (int, optional): Max new tokens after the prompt to generate. Defaults to 128.
        do_sample (bool, optional): Whether or not to use sampling. Defaults to True.
        temperature (float, optional): The value used to modulate the next token probabilities.
            Defaults to 1.0
        top_p (float, optional): If set to float < 1, only the smallest set of most probable tokens with
            probabilities that add up to top_p or higher are kept for generation. Defaults to 1.0.
        top_k (int, optional): The number of highest probability vocabulary tokens to keep for top-k-filtering.
            Defaults to 50.
        num_return_sequences (int, optional): The number of independently computed returned sequences for each
            element in the batch. Defaults to 1.
    """
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
    """
    Initialize the pipeline
    Uses Hugging Face GenerationConfig defaults
        https://huggingface.co/docs/transformers/v4.29.1/en/main_classes/text_generation#transformers.GenerationConfig
    Args:
        model (transformers.AutoModelForCausalLM): Falcon model for text generation
        tokenizer (transformers.AutoTokenizer): Tokenizer for model
        prompt (str): Prompt for text generation
        eos_token_ids (List[int]): the eos_token(s) for the text generation
        max_new_tokens (int, optional): Max new tokens after the prompt to generate. Defaults to 128.
        do_sample (bool, optional): Whether or not to use sampling. Defaults to True.
        temperature (float, optional): The value used to modulate the next token probabilities.
            Defaults to 1.0
        top_p (float, optional): If set to float < 1, only the smallest set of most probable tokens with
            probabilities that add up to top_p or higher are kept for generation. Defaults to 1.0.
        top_k (int, optional): The number of highest probability vocabulary tokens to keep for top-k-filtering.
            Defaults to 50.
        num_return_sequences (int, optional): The number of independently computed returned sequences for each
            element in the batch. Defaults to 1.
    """
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
    """
    Initialize the pipeline
    Uses Hugging Face GenerationConfig defaults
        https://huggingface.co/docs/transformers/v4.29.1/en/main_classes/text_generation#transformers.GenerationConfig
    Args:
        model (transformers.AutoModelForCausalLM): Falcon model for text generation
        tokenizer (transformers.AutoTokenizer): Tokenizer for model
        prompt (str): Prompt for text generation
        eos_token_ids (List[int]): the eos_token(s) for the text generation
        max_new_tokens (int, optional): Max new tokens after the prompt to generate. Defaults to 128.
        do_sample (bool, optional): Whether or not to use sampling. Defaults to True.
        temperature (float, optional): The value used to modulate the next token probabilities.
            Defaults to 1.0
        top_p (float, optional): If set to float < 1, only the smallest set of most probable tokens with
            probabilities that add up to top_p or higher are kept for generation. Defaults to 1.0.
        top_k (int, optional): The number of highest probability vocabulary tokens to keep for top-k-filtering.
            Defaults to 50.
        num_return_sequences (int, optional): The number of independently computed returned sequences for each
            element in the batch. Defaults to 1.
    """
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
    """
    Initialize the pipeline
    Uses Hugging Face GenerationConfig defaults
        https://huggingface.co/docs/transformers/v4.29.1/en/main_classes/text_generation#transformers.GenerationConfig
    Args:
        model (transformers.AutoModelForCausalLM): Falcon model for text generation
        tokenizer (transformers.AutoTokenizer): Tokenizer for model
        prompt (str): Prompt for text generation
        eos_token_ids (List[int]): the eos_token(s) for the text generation
        max_new_tokens (int, optional): Max new tokens after the prompt to generate. Defaults to 128.
        do_sample (bool, optional): Whether or not to use sampling. Defaults to True.
        temperature (float, optional): The value used to modulate the next token probabilities.
            Defaults to 1.0
        top_p (float, optional): If set to float < 1, only the smallest set of most probable tokens with
            probabilities that add up to top_p or higher are kept for generation. Defaults to 1.0.
        top_k (int, optional): The number of highest probability vocabulary tokens to keep for top-k-filtering.
            Defaults to 50.
        num_return_sequences (int, optional): The number of independently computed returned sequences for each
            element in the batch. Defaults to 1.
    """
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
