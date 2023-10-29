# LLM-reasoning-pop-quiz

[![License](https://img.shields.io/badge/License-Apache_2.0-green.svg)](https://github.com/daniel-furman/Polyglot-or-Not/blob/main/LICENSE) 
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/release/python-390/) 
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black) 

---

## Test Leaderboard

| model   | size |	alignment | alpaca eval (win rate %)    | pop quiz score (**here**)    | test date    | 
|----------|:--------------:|--------------|:--------------:|:-------------:|:--------------:|
| `openai/gpt-4`                       |     -      |    RLHF  |   	95.28      |    -       | -   |
| `meta-llama/Llama-2-70b-chat-hf`     |    70B     |    RLHF  |   	92.66      |   -        | -   |
| `anthropic/claude-2`                 |     -      |    RLHF  |   	91.36      |    -       | -   |
| `openai/gpt-3.5`                     |    -       |    RLHF  |  	81.71      |    -       | -   |
| `HuggingFaceH4/zephyr-7b-beta`       |     7B     |    dDPO  |   	90.60      |   -        | -   |
| `mistralai/mistral-7b-instruct-v0.1` |   7B       |    SFT   |   	-          |    -       | -   |
| `HuggingFaceH4/mistral-7b-sft-beta`  |    7B      |    dSFT  |   	-          |   -        | -   |
| `dfurman/mistral-7b-instruct-peft`   |    7B      |    dSFT  |   	-          |   -        | -   |

<br>

## Questions with Answers

**NB**: Only the top performing models are shown in the responses below. See the ```notebooks``` folder for more results.

### Section 1. Zero-shot CoT reasoning

* From [https://arxiv.org/abs/2205.11916](https://arxiv.org/abs/2205.11916)

**1.1** A juggler has 16 balls. Half of the balls are golf balls and half of the golf balls are blue. How many blue golf balls are there?\nRespond as succinctly as possible. Let's think step by step.

| model                        |  response             | correct  |
|------------------------------|-----------------------|:---------:|
| `openai/gpt-4`               | - | - |
| `mistralai/mistral-7b-instruct-v0.1`         | - | - |

<br>

**1.2** Daniel is in need of a haircut. His barber works Mondays, Wednesdays, and Fridays. So, Daniel went in for a haircut on Sunday. Does this make logical sense?\nRespond as succinctly as possible. Let's think step by step.

| model                        |  response             | correct  |
|------------------------------|-----------------------|:---------:|
| `openai/gpt-4`               |  - | - |
| `mistralai/mistral-7b-instruct-v0.1` | - | - |

### Section 2. Least to most prompting

* From [https://arxiv.org/abs/2205.10625](https://arxiv.org/abs/2205.10625)


**2.1**: It takes Amy 4 minutes to climb to the top of a slide. It takes her 1 minute to slide down. How long does each trip take?\nRespond as succinctly as possible. Let's think step by step. `{insert response #1}` The slide closes in 15 minutes. How many times can she slide before it closes?\nRespond as succinctly as possible. Let's think step by step. `{insert response #2}`

Response #1:

| model                        | response             | correct   |
|------------------------------|----------------------|:---------:|
| `openai/gpt-4`               |  - | - |
| `mistralai/mistral-7b-instruct-v0.1` | - | - |

Response #2:

| model                        | response             | correct   |
|------------------------------|----------------------|:---------:|
| `openai/gpt-4`               |  - | - |
| `mistralai/mistral-7b-instruct-v0.1` | - | - |
<br>

**2.2**: It takes Ben 10 minutes to drive to the store. It then takes him 4 minutes to find parking before he can start shopping. How long before he can start shopping?\nRespond as succinctly as possible. Let's think step by step. `{insert response #1}` The store closes in an hour. Can he make to the store before it closes?\nRespond as succinctly as possible. Let's think step by step. `{insert response #2}`

Response #1:

| model                        | response             | correct   |
|------------------------------|----------------------|:---------:|
| `openai/gpt-4`               |  - | - |
| `mistralai/mistral-7b-instruct-v0.1` | - | - |

Response #2:

| model                        | response             | correct   |
|------------------------------|----------------------|:---------:|
| `openai/gpt-4`               |  - | - |
| `mistralai/mistral-7b-instruct-v0.1` | - | - |

<br>

### Section 3. Tabular Chain of Thought

* From [https://arxiv.org/abs/2305.17812](https://arxiv.org/abs/2305.17812)

**3.1**: Jackson is planting tulips. He can fit 6 red tulips in a row and 8 blue tulips in a row. If Jackson buys 36 red tulips and 24 blue tulips, how many rows of flowers will he plant?\nRespond as succinctly as possible. Format the response as a completion of this table.\n|step|subquestion|procedure|result|\n|:---|:----------|:--------|:-----:|.

`openai/gpt-4` (✔️): 


-


`mistralai/mistral-7b-instruct-v0.1` (✔️): 

-

**3.2**: The bakers at the Beverly Hills Bakery baked 200 loaves of bread on Monday morning. They sold 93 loaves in the morning and 39 loaves in the afternoon. A grocery store then returned 6 unsold loaves back to the bakery. How many loaves of bread did the bakery have left?\nRespond as succinctly as possible. Format the response as a completion of this table.\n|step|subquestion|procedure|result|\n|:---|:----------|:--------|:-----:|.

`openai/gpt-4` (✔️): 

-


`mistralai/mistral-7b-instruct-v0.1` (ⅹ): 

-