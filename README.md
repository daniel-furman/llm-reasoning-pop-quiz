# LLM-reasoning-pop-quiz

[![License](https://img.shields.io/badge/License-Apache_2.0-green.svg)](https://github.com/daniel-furman/Polyglot-or-Not/blob/main/LICENSE) 
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/release/python-390/) 
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black) 

---

## Test Leaderboard

| model   | release date  | size |	alignment | alpaca eval (win rate %)    | pop quiz score    | test date    | 
|----------|--------------|:--------------:|--------------|:--------------:|:-------------:|--------------|
| `openai/gpt-4`                       | Mar 2023     |    -      |    RLHF  |   	95.28      |    8/8   | 10/01/2023   |
| `anthropic/claude-2`                 | Jul 2023     |    -      |    RLHF  |   	91.36      |    7/8    | 10/01/2023   |
| `mistralai/mistral-7b-instruct-v0.1` | Sep 2023     |    7B     |    SFT   |   	-          |   7/8     | 10/01/2023   |
| `HuggingFaceH4/mistral-7b-sft-beta`  | Oct 2023     |    7B     |    dSFT  |   	-          |   -       | 10/28/2023   |
| `HuggingFaceH4/zephyr-7b-beta`       | Oct 2023     |    7B     |    dDPO  |   	90.60      |   -       | 10/28/2023   |
| `meta-llama/Llama-2-70b-chat-hf`     | Jul 2023     |    13B    |    RLHF  |   	92.66      |   -       | 10/28/2023   |
| `dfurman/mistral-7b-instruct-peft`   | Sep 2023     |    7B     |    dSFT  |   	-          |   -       | 10/28/2023   |


<br>

## Questions with Answers

### Section 1. CoT reasoning zero-shot

* From [https://arxiv.org/abs/2205.11916](https://arxiv.org/abs/2205.11916)

**1.1** A juggler has 16 balls. Half of the balls are golf balls and half of the golf balls are blue. How many blue golf balls are there? Let's think step by step.

| model                        |  response             | correct  |
|------------------------------|-----------------------|:---------:|
| `openai/gpt-4`               | 1. Half of the 16 balls are golf balls: $\( \frac{16}{2} = 8 \)$ golf balls.<br /> 2. Half of the golf balls are blue: $\( \frac{8}{2} = 4 \)$ blue golf balls.| ✔ |
| `anthropic/claude-2`         | • 16 total balls<br /> • Half are golf balls: 8<br /> • Half of those are blue: 4<br /> • So there are 4 blue golf balls.| ✔ |
| `mistralai/mistral-7b-instruct-v0.1`         | Let's break down the information given:<br />1. There are 16 balls in total.<br />2. Half of the balls are golf balls.<br />3. Half of the golf balls are blue.<br /><br />Now let's apply this logic:<br />1. We know that half of the balls are golf balls, so there are 16 / 2 = 8 golf balls.<br />2. Half of these golf balls are blue, so there are 8 / 2 = 4 blue golf balls.<br /><br />Final answer: There are 4 blue golf balls. | ✔ |

<br>

**1.2** Daniel is in need of a haircut. His barber works Mondays, Wednesdays, and Fridays. So, Daniel went in for a haircut on Sunday. Does this make logical sense? Let's think step by step.

| model                        |  response             | correct  |
|------------------------------|-----------------------|:---------:|
| `openai/gpt-4`               | No, it does not make logical sense for Daniel to go in for a haircut on Sunday when his barber works on Mondays, Wednesdays, and Fridays.| ✔ |
| `anthropic/claude-2`         | • Daniel needs a haircuts<br /> • His barber works Mondays, Wednesdays, Fridays<br /> • Daniel went for a haircut on Sunday<br /> • The barber doesn't work Sundays<br /> • So it's illogical that Daniel went on a day the barber doesn't work.<br /> • Therefore, no it does not make logical sense.| ✔ |
| `mistralai/mistral-7b-instruct-v0.1` | No, this does not make logical sense. Daniel's barber works on Mondays, Wednesdays, and Fridays, so he would not be available on Sunday for a haircut. Daniel would need to go to the barber on one of those days. | ✔ |



<br>

### Section 2. Least to most prompting

* From [https://arxiv.org/abs/2205.10625](https://arxiv.org/abs/2205.10625)


**2.1**: It takes Amy 4 minutes to climb to the top of a slide. It takes her 1 minute to slide down. How long does each trip take? Let's think step by step. `{insert response #1}` The slide closes in 15 minutes. How many times can she slide before it closes? Let's think step by step. `{insert response #2}`

Response #1:

| model                        | response             | correct   |
|------------------------------|----------------------|:---------:|
| `openai/gpt-4`               | A: Each trip (climbing up and sliding down) for Amy takes a total of 5 minutes (4 minutes to climb up + 1 minute to slide down).| ✔ |
| `anthropic/claude-2`         | • Amy takes 4 minutes to climb up the slide<br /> • She takes 1 minute to slide down<br /> • So each trip up and down takes 4 + 1 = 5 minutes<br /> • Therefore, each trip takes 5 minutes. | ✔ |
| `mistralai/mistral-7b-instruct-v0.1` | Each trip takes 5 minutes. | ✔ |

Response #2:

| model                        | response             | correct   |
|------------------------------|----------------------|:---------:|
| `openai/gpt-4`               | A: Amy takes 5 minutes for one complete cycle of climbing up and sliding down. If the slide closes in 15 minutes, she can make $\(\frac{15}{5} = 3\)$ trips before it closes.| ✔ |
| `anthropic/claude-2`         | Okay, let's think through this:<br /><br /> • It takes Amy 5 minutes for each trip up and down the slide<br /> • The slide closes in 15 minutes<br /> • To figure out how many full trips Amy can take, we divide the total time by the time per trip:<br /> • 15 minutes / 5 minutes per trip = 3 trip<br /><br />Therefore, if the slide closes in 15 minutes, Amy can slide 3 times before it closes.| ✔ |
| `mistralai/mistral-7b-instruct-v0.1` | She can slide 3 times before it closes. | ✔ |

<br>

**2.2**: It takes Ben 10 minutes to drive to the store. It then takes him 4 minutes to find parking before he can start shopping. How long before he can start shopping? Let's think step by step. `{insert response #1}` The store closes in an hour. Can he make to the store before it closes? Let's think step by step. `{insert response #2}`

Response #1:

| model                        | response             | correct   |
|------------------------------|----------------------|:---------:|
| `openai/gpt-4`               | A: Ben takes 10 minutes to drive to the store and an additional 4 minutes to find parking, so before he can start shopping it takes him a total of 10 minutes + 4 minutes = 14 minutes. | ✔ |
| `anthropic/claude-2`         | • Ben takes 10 minutes to drive to the store<br /> • He then takes 4 minutes to find parking<br /> • So the total time before he can start shopping is 10 + 4 = 14 minutes<br /><br />Therefore, the total time before Ben can start shopping is 14 minutes.| ✔ |
| `mistralai/mistral-7b-instruct-v0.1` | Ben needs to wait 14 minutes before he can start shopping. | ✔ |

Response #2:

| model                        | response             | correct   |
|------------------------------|----------------------|:---------:|
| `openai/gpt-4`               | A: Yes, if Ben takes 14 minutes to get to the store and start shopping, he will make it before the store closes, as an hour (60 minutes) is sufficient time for this journey. | ✔ |
| `anthropic/claude-2`         | Okay, let's break this down:<br /><br /> • It takes Ben 14 minutes total before he can start shopping (10 minutes to drive + 4 minutes to park)<br /> •The store closes in 1 hour<br /> • So Ben has 1 hour - 14 minutes = 46 minutes to shop before the store closes<br /><br />Since Ben has 46 minutes to shop before the store closes, and it only took him 14 minutes to get there, yes he can make it to the store before it closes.| ✔ |
| `mistralai/mistral-7b-instruct-v0.1` | Yes, Ben can make it to the store before it closes. | ✔ |

<br>

### Section 3. Tabular Chain of Thought

* From [https://arxiv.org/abs/2305.17812](https://arxiv.org/abs/2305.17812)

**3.1**: Jackson is planting tulips. He can fit 6 red tulips in a row and 8 blue tulips in a row. If Jackson buys 36 red tulips and 24 blue tulips, how many rows of flowers will he plant? Let's think step by step. Format the response as a completion of this table.\n|step|subquestion|procedure|result|\n|:---|:----------|:--------|:-----:|.

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

`mistralai/mistral-7b-instruct-v0.1` (✔️): 

|step|subquestion|procedure|result|
|:---|:----------|:--------|:-----:|
|1.|How many rows of red tulips can Jackson plant?|Divide the number of red tulips by the number of red tulips per row.|36/6 = 6 rows of red tulips.|
|2.|How many rows of blue tulips can Jackson plant?|Divide the number of blue tulips by the number of blue tulips per row.|24/8 = 3 rows of blue tulips.|
|3.|How many rows of flowers can Jackson plant in total?|Add the number of rows of red tulips and blue tulips.|6 + 3 = 9 rows of flowers.|

**3.2**: The bakers at the Beverly Hills Bakery baked 200 loaves of bread on Monday morning. They sold 93 loaves in the morning and 39 loaves in the afternoon. A grocery store then returned 6 unsold loaves back to the bakery. How many loaves of bread did the bakery have left? Format the response as a completion of this table.\n|step|subquestion|procedure|result|\n|:---|:----------|:--------|:-----:|.

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

`anthropic/claude-2` (ⅹ): 

A: Here is the completed table showing the steps to solve this math word problem:

|step|subquestion|procedure|result
|:---|:----------|:--------|:-----:|
|1|How many loaves did the bakery bake on Monday morning?|Given in the problem|200 loaves
|2|How many loaves did they sell in the morning?|Given in the problem|93 loaves
|3|How many loaves did they sell in the afternoon?|Given in the problem|39 loaves  
|4|How many unsold loaves were returned?|Given in the problem|6 loaves
|5|How many loaves were sold total?|Morning sales + afternoon sales|93 + 39 = 132 loaves
|6|How many baked loaves remain?|Original loaves - sold loaves - returned loaves|200 - 132 - 6 = 62 loaves

`mistralai/mistral-7b-instruct-v0.1` (ⅹ): 

|step|subquestion|procedure|result|
|:---|:----------|:--------|:-----:|
|1.|How many loaves of bread did the bakery have initially?|The bakery baked 200 loaves on Monday morning.|200|
|2.|How many loaves of bread did the bakery sell in the morning?|The bakery sold 93 loaves in the morning.|93|
|3.|How many loaves of bread did the bakery sell in the afternoon?|The bakery sold 39 loaves in the afternoon.|39|
|4.|How many loaves of bread did the bakery have left after selling in the morning and afternoon?|The bakery had 93 + 39 = 132 loaves left after selling in the morning and afternoon.|132|
|5.|How many loaves of bread did the grocery store return?|The grocery store returned 6 unsold loaves back to the bakery.|6|
|6.|How many loaves of bread did the bakery have left after the grocery store returned?|The bakery had 132 - 6 = 126 loaves left after the grocery store returned.|126|"
