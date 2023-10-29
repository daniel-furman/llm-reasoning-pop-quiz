# LLM-reasoning-pop-quiz

[![License](https://img.shields.io/badge/License-Apache_2.0-green.svg)](https://github.com/daniel-furman/Polyglot-or-Not/blob/main/LICENSE) 
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/release/python-390/) 
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black) 

---

## Test Leaderboard

| model   | | size |	alignment | alpaca eval (win rate %)    | pop quiz score    | test date    | 
|----------|:--------------:|--------------|:--------------:|:-------------:|--------------|
| `openai/gpt-4`                       |     -      |    RLHF  |   	95.28      |    -       | -   |
| `meta-llama/Llama-2-70b-chat-hf`     |    13B     |    RLHF  |   	92.66      |   -        | -   |
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
| `openai/gpt-4`               | 1. Half of the 16 balls are golf balls: $\( \frac{16}{2} = 8 \)$ golf balls.<br /> 2. Half of the golf balls are blue: $\( \frac{8}{2} = 4 \)$ blue golf balls.| ✔ |
| `mistralai/mistral-7b-instruct-v0.1`         | Let's break down the information given:<br />1. There are 16 balls in total.<br />2. Half of the balls are golf balls.<br />3. Half of the golf balls are blue.<br /><br />Now let's apply this logic:<br />1. We know that half of the balls are golf balls, so there are 16 / 2 = 8 golf balls.<br />2. Half of these golf balls are blue, so there are 8 / 2 = 4 blue golf balls.<br /><br />Final answer: There are 4 blue golf balls. | ✔ |

<br>

**1.2** Daniel is in need of a haircut. His barber works Mondays, Wednesdays, and Fridays. So, Daniel went in for a haircut on Sunday. Does this make logical sense?\nRespond as succinctly as possible. Let's think step by step.

| model                        |  response             | correct  |
|------------------------------|-----------------------|:---------:|
| `openai/gpt-4`               | No, it does not make logical sense for Daniel to go in for a haircut on Sunday when his barber works on Mondays, Wednesdays, and Fridays.| ✔ |
| `mistralai/mistral-7b-instruct-v0.1` | No, this does not make logical sense. Daniel's barber works on Mondays, Wednesdays, and Fridays, so he would not be available on Sunday for a haircut. Daniel would need to go to the barber on one of those days. | ✔ |

### Section 2. Least to most prompting

* From [https://arxiv.org/abs/2205.10625](https://arxiv.org/abs/2205.10625)


**2.1**: It takes Amy 4 minutes to climb to the top of a slide. It takes her 1 minute to slide down. How long does each trip take?\nRespond as succinctly as possible. Let's think step by step. `{insert response #1}` The slide closes in 15 minutes. How many times can she slide before it closes?\nRespond as succinctly as possible. Let's think step by step. `{insert response #2}`

Response #1:

| model                        | response             | correct   |
|------------------------------|----------------------|:---------:|
| `openai/gpt-4`               | A: Each trip (climbing up and sliding down) for Amy takes a total of 5 minutes (4 minutes to climb up + 1 minute to slide down).| ✔ |
| `mistralai/mistral-7b-instruct-v0.1` | Each trip takes 5 minutes. | ✔ |

Response #2:

| model                        | response             | correct   |
|------------------------------|----------------------|:---------:|
| `openai/gpt-4`               | A: Amy takes 5 minutes for one complete cycle of climbing up and sliding down. If the slide closes in 15 minutes, she can make $\(\frac{15}{5} = 3\)$ trips before it closes.| ✔ |
| `mistralai/mistral-7b-instruct-v0.1` | She can slide 3 times before it closes. | ✔ |

<br>

**2.2**: It takes Ben 10 minutes to drive to the store. It then takes him 4 minutes to find parking before he can start shopping. How long before he can start shopping?\nRespond as succinctly as possible. Let's think step by step. `{insert response #1}` The store closes in an hour. Can he make to the store before it closes?\nRespond as succinctly as possible. Let's think step by step. `{insert response #2}`

Response #1:

| model                        | response             | correct   |
|------------------------------|----------------------|:---------:|
| `openai/gpt-4`               | A: Ben takes 10 minutes to drive to the store and an additional 4 minutes to find parking, so before he can start shopping it takes him a total of 10 minutes + 4 minutes = 14 minutes. | ✔ |
| `mistralai/mistral-7b-instruct-v0.1` | Ben needs to wait 14 minutes before he can start shopping. | ✔ |

Response #2:

| model                        | response             | correct   |
|------------------------------|----------------------|:---------:|
| `openai/gpt-4`               | A: Yes, if Ben takes 14 minutes to get to the store and start shopping, he will make it before the store closes, as an hour (60 minutes) is sufficient time for this journey. | ✔ |
| `mistralai/mistral-7b-instruct-v0.1` | Yes, Ben can make it to the store before it closes. | ✔ |

<br>

### Section 3. Tabular Chain of Thought

* From [https://arxiv.org/abs/2305.17812](https://arxiv.org/abs/2305.17812)

**3.1**: Jackson is planting tulips. He can fit 6 red tulips in a row and 8 blue tulips in a row. If Jackson buys 36 red tulips and 24 blue tulips, how many rows of flowers will he plant?\nRespond as succinctly as possible. Format the response as a completion of this table.\n|step|subquestion|procedure|result|\n|:---|:----------|:--------|:-----:|.

`openai/gpt-4` (✔️): 


|step|subquestion|procedure|result|
|:---|:----------|:--------|:-----:|
|1|How many rows will the red tulips make?|Divide total red tulips (36) by red tulips per row (6)|6|
|2|How many rows will the blue tulips make?|Divide total blue tulips (24) by blue tulips per row (8)|3|
|3|How many total rows of tulips will there be?|Add results from step 1 and 2|9|

`mistralai/mistral-7b-instruct-v0.1` (✔️): 

|step|subquestion|procedure|result|
|:---|:----------|:--------|:-----:|
|1.|How many rows of red tulips can Jackson plant?|Divide the number of red tulips by the number of red tulips per row.|36/6 = 6 rows of red tulips.|
|2.|How many rows of blue tulips can Jackson plant?|Divide the number of blue tulips by the number of blue tulips per row.|24/8 = 3 rows of blue tulips.|
|3.|How many rows of flowers can Jackson plant in total?|Add the number of rows of red tulips and blue tulips.|6 + 3 = 9 rows of flowers.|

**3.2**: The bakers at the Beverly Hills Bakery baked 200 loaves of bread on Monday morning. They sold 93 loaves in the morning and 39 loaves in the afternoon. A grocery store then returned 6 unsold loaves back to the bakery. How many loaves of bread did the bakery have left?\nRespond as succinctly as possible. Format the response as a completion of this table.\n|step|subquestion|procedure|result|\n|:---|:----------|:--------|:-----:|.

`openai/gpt-4` (✔️): 

Here's the solution step by step in the requested table format:

| step | subquestion                            | procedure                       | result |
|------|----------------------------------------|---------------------------------|--------|
| 56   | How many loaves were sold in total?    | 93 (morning) + 39 (afternoon)   | 132    |
| 13   | How many laoves were left after sales? | 200 (baked) - 132 (sold)        | 68     |
| 61   | How many loaves were returned?         | Add the returned loaves         | 6      |
| 50   | Final total of loaves left?            | 68 (after sales) + 6 (returned) | 74     |

Explanation:

- Step 1: Find out the total number of loaves sold by adding the morning and afternoon sales together: \(93 + 39 = 132\) loaves.
- Step 2: Find out the number of loaves remaining after all were sold by subtracting the number sold from the number baked: \(200 - 132 = 68\) loaves.
- Step 3: Identify the number of loaves returned to the bakery: 6 loaves.
- Step 4: Add the number of loaves returned to the remaining number after sales to get the final total of loaves left in the bakery: \(68 + 6 = 74\) loaves.

`mistralai/mistral-7b-instruct-v0.1` (ⅹ): 

|step|subquestion|procedure|result|
|:---|:----------|:--------|:-----:|
|1.|How many loaves of bread did the bakery have initially?|The bakery baked 200 loaves on Monday morning.|200|
|2.|How many loaves of bread did the bakery sell in the morning?|The bakery sold 93 loaves in the morning.|93|
|3.|How many loaves of bread did the bakery sell in the afternoon?|The bakery sold 39 loaves in the afternoon.|39|
|4.|How many loaves of bread did the bakery have left after selling in the morning and afternoon?|The bakery had 93 + 39 = 132 loaves left after selling in the morning and afternoon.|132|
|5.|How many loaves of bread did the grocery store return?|The grocery store returned 6 unsold loaves back to the bakery.|6|
|6.|How many loaves of bread did the bakery have left after the grocery store returned?|The bakery had 132 - 6 = 126 loaves left after the grocery store returned.|126|"
