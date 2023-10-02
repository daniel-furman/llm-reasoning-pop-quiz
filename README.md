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
| `tiiuae/falcon-40b-instruct`         | May 2023     |     xx        |
| `mosaicml/mpt-30b-instruct`          | Jun 2023     |     xx        |
| `meta-llama/Llama-2-70b-chat-hf`     | Jul 2023     |     xx        |
| `meta-llama/Llama-2-13b-chat-hf`     | Jul 2023     |     xx        |
| `meta-llama/Llama-2-7b-chat-hf`      | Jul 2023     |     xx        |
| `mistralai/Mistral-7B-Instruct-v0.1` | Sep 2023     |     xx        |

<br>

## Questions with Answers

### Section 1. CoT reasoning zero-shot

* From [https://arxiv.org/abs/2205.11916](https://arxiv.org/abs/2205.11916)

**1.1** Q: A juggler has 16 balls. Half of the balls are golf balls and half of the golf balls are blue. How many blue golf balls are there? A: Take a deep breath and work on this problem step-by-step. Respond succinctly.

| model                        |  response             | correct  |
|------------------------------|-----------------------|:---------:|
| `openai/gpt-4`               | 1. Half of the 16 balls are golf balls: $\( \frac{16}{2} = 8 \)$ golf balls.<br /> 2. Half of the golf balls are blue: $\( \frac{8}{2} = 4 \)$ blue golf balls.| ✔ |
| `anthropic/claude-2`         | • 16 total balls<br /> • Half are golf balls: 8<br /> • Half of those are blue: 4<br /> • So there are 4 blue golf balls.| ✔ |

<br>

**1.2** Q: Daniel is in need of a haircut. His barber works Mondays, Wednesdays, and Fridays. So, Daniel went in for a haircut on Sunday. Does this make logical sense? A: Take a deep breath and work on this problem step-by-step. Respond succinctly.

| model                        |  response             | correct  |
|------------------------------|-----------------------|:---------:|
| `openai/gpt-4`               | No, it does not make logical sense for Daniel to go in for a haircut on Sunday when his barber works on Mondays, Wednesdays, and Fridays.| ✔ |
| `anthropic/claude-2`         | • Daniel needs a haircuts<br /> • His barber works Mondays, Wednesdays, Fridays<br /> • Daniel went for a haircut on Sunday<br /> • The barber doesn't work Sundays<br /> • So it's illogical that Daniel went on a day the barber doesn't work.<br /> • Therefore, no it does not make logical sense.| ✔ |

<br>

### Section 2. CoT reasoning with few-shot examples

* From [https://ai.googleblog.com/2022/05/language-models-perform-reasoning-via.html](https://ai.googleblog.com/2022/05/language-models-perform-reasoning-via.html)

**2.1** Q: Roger has 5 tennis balls. He buys 2 more cans of tennis balls. Each can has 3 tennis balls. How many tennis balls does have now? A: Take a deep breath and work on this problem step-by-step. Respond succinctly. Roger started with 5 balls. 2 cans of 3 tennis balls each is 6 tennis balls. 5 + 6 = 11. The answer is 11. Q: The cafeteria had 23 apples. If they used 20 to make lunch and bought 6 more, how many apples do they have? A: Take a deep breath and work on this problem step-by-step. Respond succinctly.

| model                        | response             | correct   |
|------------------------------|----------------------|:---------:|
| `openai/gpt-4`               | | |
| `anthropic/claude-2`         | | |

<br>

**2.2** Q: Roger has 3 children. Each of his kids invited 4 of their friends to come to the birthday party. All of the friends came to the party. How many children are at the party? A: Take a deep breath and work on this problem step-by-step. Respond succinctly. Roger has 3 children, each of whom came to the party. Each of them have 4 friends coming over. 3 * 4 = 12. So 12 of their friends came to the party. 12 + 3 = 15. So, there are 15 children at the party in total. The answer is 15. Q: Ben has 4 children. 50% of his kids are in college and no longer live at home. How many of Ben's children still live at home? A: Take a deep breath and work on this problem step-by-step. Respond succinctly.

| model                        | response             | correct   |
|------------------------------|----------------------|:---------:|
| `openai/gpt-4`               | | |
| `anthropic/claude-2`         | | |
<br>

### Section 3. Least to most prompting

* From [https://arxiv.org/abs/2205.10625](https://arxiv.org/abs/2205.10625)


**3.1**: Q: It takes Amy 4 minutes to climb to the top of a slide. It takes her 1 minute to slide down. How long does each trip take? A: Take a deep breath and work on this problem step-by-step. Respond succinctly. `{insert response #1}` Q: The slide closes in 15 minutes. How many times can she slide before it closes? A: Take a deep breath and work on this problem step-by-step. Respond succinctly. `{insert response #2}`

Response #1:

| model                        | response             | correct   |
|------------------------------|----------------------|:---------:|
| `openai/gpt-4`               | | |
| `anthropic/claude-2`         | | |

Response #2:

| model                        | response             | correct   |
|------------------------------|----------------------|:---------:|
| `openai/gpt-4`               | | |
| `anthropic/claude-2`         | | |

<br>

**3.2**: Q: It takes Ben 10 minutes to drive to the store. It then takes him 4 minutes to find parking before he can start shopping. How long before he can start shopping? A: Take a deep breath and work on this problem step-by-step. Respond succinctly. `{insert response #1}` Q: The store closes in an hour. Can he make to the store before it closes? A: Take a deep breath and work on this problem step-by-step. Respond succinctly. `{insert response #2}`

Response #1:

| model                        | response             | correct   |
|------------------------------|----------------------|:---------:|
| `openai/gpt-4`               | | |
| `anthropic/claude-2`         | | |

Response #2:

| model                        | response             | correct   |
|------------------------------|----------------------|:---------:|
| `openai/gpt-4`               | | |
| `anthropic/claude-2`         | | |

<br>

### Section 4. Tabular Chain of Thought

* From [https://arxiv.org/abs/2305.17812](https://arxiv.org/abs/2305.17812)

**4.1**: Q: Jackson is planting tulips. He can fit 6 red tulips in a row and 8 blue tulips in a row. If Jackson buys 36 red tulips and 24 blue tulips, how many rows of flowers will he plant? A: Take a deep breath and work on this problem step-by-step. Respond succinctly. Format the response as a completion of this table.\n|step|subquestion|procedure|result|\n|:---|:----------|:--------|:-----:|.

`openai/gpt-4` (✔️): 

|step|subquestion|procedure|result|
|:---|:----------|:--------|:-----:|
|1|How many rows will the red tulips make?|Divide total red tulips (36) by red tulips per row (6)|6|
|2|How many rows will the blue tulips make?|Divide total blue tulips (24) by blue tulips per row (8)|3|
|3|How many total rows of tulips will there be?|Add results from step 1 and 2|9|

`anthropic/claude-2` (✔️): 

Here is the step-by-step solution:

|step|subquestion|procedure|result|
|:---|:----------|:--------|:-----:|  
|1|How many red tulips did Jackson buy?|Given|36|
|2|How many red tulips fit in 1 row?|Given|6|
|3|How many rows of red tulips can be planted?|Red tulips bought / Red tulips per row|36 / 6 = 6|
|4|How many blue tulips did Jackson buy?|Given|24|
|5|How many blue tulips fit in 1 row?|Given|8|
|6|How many rows of blue tulips can be planted?|Blue tulips bought / Blue tulips per row|24 / 8 = 3|
|7|How many total rows will be planted?|Red rows + Blue rows|6 + 3 = 9|

Therefore, the total number of rows Jackson will plant is 9.

**4.2**: Q: The bakers at the Beverly Hills Bakery baked 200 loaves of bread on Monday morning. They sold 93 loaves in the morning and 39 loaves in the afternoon. A grocery store returned 6 unsold loaves, meaning they were added back to the total. How many loaves of bread did they have left? A: Take a deep breath and work on this problem step-by-step. Respond succinctly. Format the response as a completion of this table.\n|step|subquestion|procedure|result|\n|:---|:----------|:--------|:-----:|.

`openai/gpt-4` (✔️): 

|step|subquestion|procedure|result|
|:---|:----------|:--------|:-----:|
|1|How many loaves were sold in the morning?|Given in problem statement|93|
|2|How many loaves were sold in the afternoon?|Given in problem statement|39|
|3|How many loaves were sold in total on Monday?|Add results from step 1 and 2|132|
|4|How many unsold loaves were returned?|Given in problem statement|6|
|5|How many loaves were left after all sales, before returns?|Subtract result from step 3 from initial 200|68|
|6|How many loaves were left after returns were added back?|Add results from step 4 and 5|74|

`anthropic/claude-2` (✔️): 

Here is the step-by-step solution:

|step|subquestion|procedure|result|  
|:---|:----------|:--------|:-----:|
|1|How many loaves did they bake originally?|Given|200|
|2|How many loaves did they sell in the morning?|Given|93|  
|3|How many loaves did they sell in the afternoon?|Given|39|
|4|How many unsold loaves were returned?|Given|6|
|5|How many loaves were sold total?|Morning sales + Afternoon sales|93 + 39 = 132|
|6|How many loaves came back unsold?|Given|6|  
|7|What is the total inventory now?|Original baked - Total sold + Unsold returned|200 - 132 + 6 = 74|

Therefore, the number of loaves they had left is 74.

