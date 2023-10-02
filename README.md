# LLM-reasoning-pop-quiz

[![License](https://img.shields.io/badge/License-Apache_2.0-green.svg)](https://github.com/daniel-furman/Polyglot-or-Not/blob/main/LICENSE) 
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/release/python-390/) 
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black) 

---

## Test Leaderboard

| model                                | release date | quiz score |
|--------------------------------------|--------------|:-------------:|
| `openai/gpt-4`                       | Mar 2023     |     xx        |
| `anthropic/claude-2`                 | Jul 2023     |     xx        |
| `openai/gpt-3.5`                     | Nov 2022     |     xx        |
| `tiiuae/falcon-40b-instruct`         | May 2023     |     xx        |
| `mosaicml/mpt-30b-instruct`          | Jun 2023     |     xx        |
| `google/flan-t5-xxl`                 | Sep 2021     |     xx        |
| `mistralai/Mistral-7B-Instruct-v0.1` | Sep 2023     |     xx        |
| `meta-llama/Llama-2-70b-chat-hf`     | Jul 2023      |     xx       |
| `meta-llama/Llama-2-13b-chat-hf`     | Jul 2023     |     xx        |
| `meta-llama/Llama-2-7b-chat-hf`      | Jul 2023     |     xx        |



<br>

## Questions with Answers

### Section 1. Zero-shot reasoning conditioned on good performance

* From [https://arxiv.org/abs/2205.11916](https://arxiv.org/abs/2205.11916)

**1.1** Q: A juggler has 16 balls. Half of the balls are golf balls and half of the golf balls are blue. How many blue golf balls are there? A: Take a deep breath and work on this problem step-by-step. Respond succinctly.

| model                        |  | response             | correct  
|------------------------------|--------------------------|:---------:
| `openai/gpt-4`               | 1. Half of the 16 balls are golf balls: $\( \frac{16}{2} = 8 \)$ golf balls.<br /> 2. Half of the golf balls are blue: $\( \frac{8}{2} = 4 \)$ blue golf balls.| ✔ |
| `anthropic/claude-2`         | • 16 total balls<br /> • Half are golf balls: 8<br /> • Half of those are blue: 4<br /> • So there are 4 blue golf balls.| ✔ |

<br>

**1.2** Q: Daniel is in need of a haircut. His barber works Mondays, Wednesdays, and Fridays. So, Daniel went in for a haircut on Sunday. Does this make logical sense? A: Take a deep breath and work on this problem step-by-step. Respond succinctly.

| model                        | correct   | response             |
|------------------------------|:---------:|--------------------------|
| `openai/gpt-4`               | | |
| `anthropic/claude-2`         | | |

<br>

**1.3** Q: The bakers at the Beverly Hills Bakery baked 200 loaves of bread on Monday morning. They sold 93 loaves in the morning and 39 loaves in the afternoon. A grocery store returned 6 unsold loaves. How many loaves of bread did they have left? A: Take a deep breath and work on this problem step-by-step. Respond succinctly.

| model                        | correct   | response             |
|------------------------------|:---------:|--------------------------|
| `openai/gpt-4`               | | |
| `anthropic/claude-2`         | | |

<br>

### Section 2. Chain-of-thought reasoning with few-shot examples

* From [https://ai.googleblog.com/2022/05/language-models-perform-reasoning-via.html](https://ai.googleblog.com/2022/05/language-models-perform-reasoning-via.html)

**2.1** Q: Roger has 5 tennis balls. He buys 2 more cans of tennis balls. Each can has 3 tennis balls. How many tennis balls does have now? A: Take a deep breath and work on this problem step-by-step. Respond succinctly. Roger started with 5 balls. 2 cans of 3 tennis balls each is 6 tennis balls. 5 + 6 = 11. The answer is 11. Q: The cafeteria had 23 apples. If they used 20 to make lunch and bought 6 more, how many apples do they have? A: Take a deep breath and work on this problem step-by-step. Respond succinctly.

| model                        | correct   | response             |
|------------------------------|:---------:|--------------------------|
| `openai/gpt-4`               | | |
| `anthropic/claude-2`         | | |

<br>

**2.2** Q: Roger has 3 children. Each of his kids invited 4 of their friends to come to the birthday party. All of the friends came to the party. How many children are at the party? A: Take a deep breath and work on this problem step-by-step. Respond succinctly. Roger has 3 children, each of whom came to the party. Each of them have 4 friends coming over. 3 * 4 = 12. So 12 of their friends came to the party. 12 + 3 = 15. So, there are 15 children at the party in total. The answer is 15. Q: Ben has 4 children. 50% of his kids are in college and no longer live at home. How many of Ben's children still live at home? A: Take a deep breath and work on this problem step-by-step. Respond succinctly.

| model                        | correct   | response             |
|------------------------------|:---------:|--------------------------|
| `openai/gpt-4`               | | |
| `anthropic/claude-2`         | | |
<br>

### Section 3. Least to most prompting

* From [https://arxiv.org/abs/2205.10625](https://arxiv.org/abs/2205.10625)


**3.1**: Q: It takes Amy 4 minutes to climb to the top of a slide. It takes her 1 minute to slide down. How long does each trip take? A: Take a deep breath and work on this problem step-by-step. Respond succinctly. `{insert response #1}` Q: The slide closes in 15 minutes. How many times can she slide before it closes? A: Take a deep breath and work on this problem step-by-step. Respond succinctly. `{insert response #2}`

Response #1:

| model                        | correct   | response             |
|------------------------------|:---------:|--------------------------|
| `openai/gpt-4`               | | |
| `anthropic/claude-2`         | | |

Response #2:

| model                        | correct   | response             |
|------------------------------|:---------:|--------------------------|
| `openai/gpt-4`               | | |
| `anthropic/claude-2`         | | |

<br>

**3.2**: Q: It takes Ben 10 minutes to drive to the store. It then takes him 4 minutes to find parking before he can start shopping. How long before he can start shopping? A: Take a deep breath and work on this problem step-by-step. Respond succinctly. `{insert response #1}` Q: The store closes in an hour. Can he make to the store before it closes? A: Take a deep breath and work on this problem step-by-step. Respond succinctly. `{insert response #2}`

Response #1:

| model                        | correct   | response             |
|------------------------------|:---------:|--------------------------|
| `openai/gpt-4`               | | |
| `anthropic/claude-2`         | | |

Response #2:

| model                        | correct   | response             |
|------------------------------|:---------:|--------------------------|
| `openai/gpt-4`               | | |
| `anthropic/claude-2`         | | |

<br>

### Section 4. Tabular Chain of Thought

* From [https://arxiv.org/abs/2305.17812](https://arxiv.org/abs/2305.17812)

**4.1**: Jackson is planting tulips. He can fit 6 red tulips in a row and 8 blue tulips in a row. If Jackson buys 36 red tulips and 24 blue tulips, how many rows of flowers will he plant? Format the response as a completion of this table.\n|step|subquestion|procedure|result|\n|:---|:----------|:--------|:-----:| `{insert response #1}`. Therefore, the answer is `{insert response #2}`.

Response #1

`openai/gpt-4`'s response (): 

`anthropic/claude-2`'s response (): 


Response #2:

| model                        | correct   | response             |
|------------------------------|:---------:|--------------------------|
| `openai/gpt-4`               | | |
| `anthropic/claude-2`         | | |