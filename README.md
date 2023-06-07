# LLM-reasoning-pop-quiz

[![License](https://img.shields.io/badge/License-Apache_2.0-green.svg)](https://github.com/daniel-furman/Polyglot-or-Not/blob/main/LICENSE) 
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/release/python-390/) 
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black) 

---

## Test Leaderboard

| model                      | release date | quiz score |
|----------------------------|--------------|:-------------:|
| `openai/gpt-4`               | Mar 2023     |     12/12       |
| `openai/gpt-3.5`             | Nov 2022     |     12/12       |
| `tiiuae/falcon-40b-instruct` | May 2023     |     10/12       |
| `google/flan-t5-xxl`         | Sep 2021     |     7/12        |

<br>

## Questions with Answers

### Section 1. Zero-shot reasoning conditioned on good performance

* From [https://arxiv.org/abs/2205.11916](https://arxiv.org/abs/2205.11916)

**1.1**: Q: A juggler has 16 balls. Half of the balls are golf balls and half of the golf balls are blue. How many blue golf balls are there? A: Let's work this out in a step by step way to be sure we have the right answer. Respond as succinctly as possible to answer the question.

| model                      | correct | response             |
|----------------------|:---------:|--------------------------|
| `openai/gpt-4`               | ✅       | Half of the 16 balls are golf balls, which is 8 balls. Half of these golf balls are blue, so there are 4 blue golf balls. |
| `openai/gpt-3.5`             | ✅       | There are 4 blue golf balls.                                                                                              |
| `tiiuae/falcon-40b-instruct` | ✅       | There are 8 golf balls in total. Half of the golf balls are blue, so there are 4 blue golf balls. |       
| `google/flan-t5-xxl` | ✅       | The juggler has 16 golf balls * 1 / 2 = 8 golf balls. There are 8 golf balls * 0.5 = 4 blue golf balls. The answer: 4.  |        

<br>

**1.2**: Q: Daniel is in need of a haircut. His barber works Mondays, Wednesdays, and Fridays. So, Daniel went in for a haircut on Sunday. Does this make logical sense? A: Let's work this out in a step by step way to be sure we have the right answer. Respond as succinctly as possible to answer the question.

| model                      | correct | response             |
|----------------------|:---------:|--------------------------|
| `openai/gpt-4`               | ✅       | No, it doesn't make logical sense because Daniel's barber does not work on Sundays. |
| `openai/gpt-3.5`             | ✅       | No, it does not make logical sense for Daniel to go in for a haircut on Sunday because his barber works on Mondays, Wednesdays, and Fridays. |
| `tiiuae/falcon-40b-instruct` | ✅       | No, it does not make logical sense for Daniel to go in for a haircut on Sunday. His barber works on Mondays, Wednesdays, and Fridays, so Daniel should have waited until one of those days to get a haircut. |
| `google/flan-t5-xxl` | ✅       | Daniel has to wait until the following week to get his haircut. The answer: no.  |        

<br>

### Section 2. Chain-of-thought reasoning with few-shot examples

* From [https://ai.googleblog.com/2022/05/language-models-perform-reasoning-via.html](https://ai.googleblog.com/2022/05/language-models-perform-reasoning-via.html)

**2.1**: Q: Roger has 5 tennis balls. He buys 2 more cans of tennis balls. Each can has 3 tennis balls. How many tennis balls does have now? A: Let's work this out in a step by step way to be sure we have the right answer. Respond as succinctly as possible to answer the question. Roger started with 5 balls. 2 cans of 3 tennis balls each is 6 tennis balls. 5 + 6 = 11. The answer is 11. Q: The cafeteria had 23 apples. If they used 20 to make lunch and bought 6 more, how many apples do they have? A: Let's work this out in a step by step way to be sure we have the right answer. Respond as succinctly as possible to answer the question.

| model                      | correct | response             |
|----------------------|:---------:|--------------------------|
| `openai/gpt-4`               | ✅       | After using 20 apples for lunch, the cafeteria has 3 apples left. With the purchase of 6 more apples, they now have 9 apples. |
| `openai/gpt-3.5`             | ✅       | The cafeteria now has 9 apples. |
| `tiiuae/falcon-40b-instruct` | ✅       | The cafeteria started with 23 apples. They used 20 to make lunch, so they have 3 apples left. They bought 6 more, so they have 9 apples now. The answer is 9. |
| `google/flan-t5-xxl` | ❌      | The cafeteria had 23 - 20 = 3 apples left after making lunch. They bought 6 + 3 = 7 apples. The answer is 7. |        


<br>

**2.2**: Q: Roger has 3 children. Each of his kids invited 4 of their friends to come to the birthday party. All of the friends came to the party. Q: How many children are at the party? A: Let's work this out in a step by step way to be sure we have the right answer. Respond as succinctly as possible to answer the question. Roger has 3 children, each of whom came to the party. Each of them have 4 friends coming over. 3 * 4 = 12. So 12 of their friends came to the party. 12 + 3 = 15. So, there are 15 children at the party in total. The answer is 15. Q: Ben has 4 children. 50% of his kids are in college and no longer live at home. Q: How many of Ben's children still live at home? A: Let's work this out in a step by step way to be sure we have the right answer. Respond as succinctly as possible to answer the question."

| model                      | correct | response             |
|----------------------|:---------:|--------------------------|
| `openai/gpt-4`               | ✅       | Ben has 4 children and 50% of them are in college and no longer live at home. Therefore, the other 50%, which is 2 children, still live at home. |
| `openai/gpt-3.5`             | ✅       | Two of Ben's children still live at home. |
| `tiiuae/falcon-40b-instruct` | ✅       | Ben has 4 children. 50% of his children are in college and no longer live at home. So, 2 of his children are in college. Therefore, 2 of his children still live at home. The answer is 2. |
| `google/flan-t5-xxl` |  ✅     | Ben has 4 children and 50% of them are in college so that's 4 *.50 = 2 children. 2 children still live at home. The answer is  2. |       

<br>

### Section 3. Least to most prompting

* From [https://arxiv.org/abs/2205.10625](https://arxiv.org/abs/2205.10625)


**3.1**: It takes Amy 4 minutes to climb to the top of a slide. It takes her 1 minute to slide down. Q: How long does each trip take? A: Let's work this out in a step by step way to be sure we have the right answer. Respond as succinctly as possible to answer the question. {insert response #1} The slide closes in 15 minutes. Q: How many times can she slide before it closes? A: Let's work this out in a step by step way to be sure we have the right answer. Respond as succinctly as possible to answer the question. {insert response #2}

Response #1:

| model                      | correct | response             |
|----------------------|:---------:|--------------------------|
| `openai/gpt-4`               | ✅       | Each trip takes Amy 5 minutes (4 minutes climbing + 1 minute sliding down). |
| `openai/gpt-3.5`             | ✅       | Each trip takes 5 minutes. |
| `tiiuae/falcon-40b-instruct` | ✅       | Amy climbs up the slide in 4 minutes, so it takes her 4 minutes to complete one trip. She slides down the slide in 1 minute, so it takes her 1 minute to complete one trip. Therefore, each trip takes 5 minutes." |
| `google/flan-t5-xxl` |  ❌     | It takes Amy 4 / 1 = 3 minutes to slide down. So each trip takes 3 / 2 = 2 minutes. The answer: 2.
 |  

Response #2:

| model                      | correct | response             |
|----------------------|:---------:|--------------------------|
| `openai/gpt-4`               | ✅       | Amy can slide 3 times before the slide closes (15 minutes total / 5 minutes per slide). |
| `openai/gpt-3.5`             | ✅       | Amy can slide down the slide 3 times before it closes. |
| `tiiuae/falcon-40b-instruct` | ✅       | Amy can slide down the slide 15/5 = 3 times before the slide closes." |
| `google/flan-t5-xxl` |  ❌     | She has 15 / 60 = 3 minutes left to slide. She can slide 3 / 3 = 2 times. The answer: 2. |

<br>

**3.2**: It takes Ben 10 minutes to drive to the store. It then takes him 4 minutes to find parking before he can start shopping. Q: How long before he can start shopping? A: Let's work this out in a step by step way to be sure we have the right answer. Respond as succinctly as possible to answer the question. {insert response #1} The store closes in an hour. Q: Can he make to the store before it closes? A: Let's work this out in a step by step way to be sure we have the right answer. Respond as succinctly as possible to answer the question. {insert response #2}

Response #1:

| model                      | correct | response             |
|----------------------|:---------:|--------------------------|
| `openai/gpt-4`               | ✅       | It takes Ben a total of 14 minutes (10 minutes driving + 4 minutes parking) to start shopping. |
| `openai/gpt-3.5`             | ✅       | Ben takes 14 minutes before he can start shopping. |
| `tiiuae/falcon-40b-instruct` | ✅       | Ben takes 10 minutes to drive to the store. He then takes 4 minutes to find parking. Therefore, it takes Ben 14 minutes to get to the store and find parking. Once he finds parking, he can start shopping. |
| `google/flan-t5-xxl` |  ✅      | It takes Ben 10 + 4 = 14 minutes to start shopping. The answer: 14. |

Response #2:

| model                      | correct | response             |
|----------------------|:---------:|--------------------------|
| `openai/gpt-4`               | ✅       | Yes, Ben can make it to the store before it closes since it only takes him 14 minutes to get there and start shopping, and the store closes in an hour. |
| `openai/gpt-3.5`             | ✅       | Yes, Ben can make it to the store before it closes. He has 46 minutes remaining before the store closes. |
| `tiiuae/falcon-40b-instruct` | ✅       | Ben has 46 minutes to shop before the store closes. He can make it to the store before it closes. |
| `google/flan-t5-xxl` |  ❌      | He has 60 minutes to get to the store. The answer: 60. |


<br>

### Section 4. Tab-CoT (Tabular Chain of Thought)

* From [https://arxiv.org/abs/2305.17812](https://arxiv.org/abs/2305.17812)

**4.1**: Jackson is planting tulips. He can fit 6 red tulips in a row and 8 blue tulips in a row. If Jackson buys 36 red tulips and 24 blue tulips, how many rows of flowers will he plant? Format the response as a completion of this table.\n|step|subquestion|procedure|result|\n|:---|:----------|:--------|:-----:| {insert response #1}. \nTherefore, the answer is {insert response #2}.

Response #1

`openai/gpt-4`'s response (✅): 

|Step|Subquestion|Procedure|Result|
|:---|:----------|:--------|:-----|
|1|How many rows of red tulips will Jackson plant?|Divide the total number of red tulips (36) by the number of red tulips per row (6).|36 / 6 = 6 rows|
|2|How many rows of blue tulips will Jackson plant?|Divide the total number of blue tulips (24) by the number of blue tulips per row (8).|24 / 8 = 3 rows|
|3|How many total rows of flowers will Jackson plant?|Add the number of rows of red tulips (6) to the number of rows of blue tulips (3).|6 + 3 = 9 rows|

`openai/gpt-3.5`'s response (✅):

| Step |       Subquestion        |             Procedure             | Result |
|:------:|:-------------------------:|:-----------------------------------:|:--------:|
|   1  | Rows of red tulips      | Divide 36 by 6 (red tulips/row)    |   6    |
|   2  | Rows of blue tulips     | Divide 24 by 8 (blue tulips/row)   |   3    |
|   3  | Total rows of flowers   | Add the results from step 1 and 2  |   9    |

`tiiuae/falcon-40b-instruct`'s response (❌):

| Step |       Subquestion        |             Procedure             | Result |
|:------:|:-------------------------:|:-----------------------------------:|:--------:|
|1|How many red tulips can Jackson fit in a row?|6|
|2|How many blue tulips can Jackson fit in a row?|8|
|3|How many red tulips did Jackson buy?|36|
|4|How many blue tulips did Jackson buy?|24|
|5|How many rows of flowers will Jackson plant?|6|
|6|How many rows of blue tulips will Jackson plant?|2|
|7|How many rows of red tulips will Jackson plant?|4|
|8|How many rows of flowers will Jackson plant in total?|6+2+4=12|

`google/flan-t5-xxl`'s response (❌):
Step 1: How many red tulips will Jackson plant? Step 2: How many blue tulips will Jackson plant? Step 3: How many rows of flowers will Jackson plant?

Response #2:

| model                      | correct | response             |
|----------------------|:---------:|--------------------------|
| `openai/gpt-4`               | ✅       | Jackson will plant 9 total rows of flowers. |
| `openai/gpt-3.5`             | ✅       | Therefore, the answer is that Jackson will plant a total of 9 rows of flowers. |
| `tiiuae/falcon-40b-instruct` | ❌       | Text generation: "12."|
| `google/flan-t5-xxl` |   ✅     | 36 red tulips / 6 red tulips / row = 6 red tulips / row. 24 blue tulips / 8 blue tulips / row = 3 blue tulips / row. 6 red tulips / row + 3 blue tulips / row = 9 rows of flowers. |

<br>

**4.2**: Example 1: Jackson is planting tulips. He can fit 6 red tulips in a row and 8 blue tulips in a row. If Jackson buys 36 red tulips and 24 blue tulips, how many rows of flowers will he plant? Format the response as a completion of this table.\n|step|subquestion|procedure|result|\n|:---|:----------|:--------|:-----:|\n|1|How many rows of red tulips will Jackson plant?|Divide the total number of red tulips (36) by the number of red tulips per row (6).|36 / 6 = 6 rows|\n|2|How many rows of blue tulips will Jackson plant?|Divide the total number of blue tulips (24) by the number of blue tulips per row (8).|24 / 8 = 3 rows|\n|3|How many total rows of flowers will Jackson plant?|Add the number of rows of red tulips (6) to the number of rows of blue tulips (3).|6 + 3 = 9 rows|. \nTherefore, the answer is Jackson will plant 9 total rows of flowers. Example 2:  Jackson is planting tulips. He can fit 3 red tulips in a row and 4 blue tulips in a row. If Jackson buys 18 red tulips and 12 blue tulips, how many rows of flowers will he plant? Format the response as a completion of this table.\n|step|subquestion|procedure|result|\n|:---|:----------|:--------|:-----:| {insert response #1}. \nTherefore, the answer is {insert response #2}.

Response #1

`openai/gpt-4`'s response (✅): 

|Step|Subquestion|Procedure|Result|
|:---|:----------|:--------|:-----|
|1|How many rows of red tulips will Jackson plant?|Divide the total number of red tulips (18) by the number of red tulips per row (3).|18 / 3 = 6 rows|
|2|How many rows of blue tulips will Jackson plant?|Divide the total number of blue tulips (12) by the number of blue tulips per row (4).|12 / 4 = 3 rows|
|3|How many total rows of flowers will Jackson plant?|Add the number of rows of red tulips (6) to the number of rows of blue tulips (3).|6 + 3 = 9 rows|

`openai/gpt-3.5`'s response (✅):

| Step |         Subquestion            |             Procedure                        | Result |
|------|-------------------------------|----------------------------------------------|--------|
|   1  | Rows of red tulips            | Divide 18 by 3 (red tulips per row)           |   6    |
|   2  | Rows of blue tulips           | Divide 12 by 4 (blue tulips per row)          |   3    |
|   3  | Total rows of flowers         | Add the results from step 1 and 2             |   9    |

`tiiuae/falcon-40b-instruct`'s response (✅):

| Step |         Subquestion            |             Procedure                        | Result |
|------|-------------------------------|----------------------------------------------|--------|
|1|How many rows of red tulips will Jackson plant?|Divide the total number of red tulips (18) by the number of red tulips per row (3).|18 / 3 = 6 rows|
|2|How many rows of blue tulips will Jackson plant?|Divide the total number of blue tulips (12) by the number of blue tulips per row (4).|12 / 4 = 3 rows|
|3|How many total rows of flowers will Jackson plant?|Add the number of rows of red tulips (6) to the number of rows of blue tulips (3).|6 + 3 = 9 rows|. 

`google/flan-t5-xxl`'s response (✅):
| Step |         Subquestion            |             Procedure                        | Result |
|------|-------------------------------|----------------------------------------------|--------|
|1|How many rows of red tulips will Jackson plant?|Divide the total number of red tulips (18) by the number of red tulips per row (3).|18 / 3 = 6 rows| 
|2|How many rows of blue tulips will Jackson plant?|Divide the total number of blue tulips (12) by the number of blue tulips per row (4).|12 / 4 = 3 rows| 
|3|How many total rows of flowers will Jackson plant?|Add the number of rows of red tulips to the number of rows of blue tulips.|6 + 3 = 9 rows|


Response #2:

| model                      | correct | response             |
|----------------------|:---------:|--------------------------|
| `openai/gpt-4`               | ✅       | In the second example, Jackson will plant 9 total rows of flowers. |
| `openai/gpt-3.5`             | ✅       | In Example 2, Jackson will also plant a total of 9 rows of flowers. |
| `tiiuae/falcon-40b-instruct` |  ✅      | Jackson will plant 9 total rows of flowers. |
| `google/flan-t5-xxl` |    ✅    | 6 + 3 = 9 rows. Therefore, the answer is Jackson will plant 9 total rows of flowers. |

**4.3**: Example 1: Jackson is planting tulips. He can fit 6 red tulips in a row and 8 blue tulips in a row. If Jackson buys 36 red tulips and 24 blue tulips, how many rows of flowers will he plant? Format the response as a completion of this table.\n|step|subquestion|procedure|result|\n|:---|:----------|:--------|:-----:|\n|1|How many rows of red tulips will Jackson plant?|Divide the total number of red tulips (36) by the number of red tulips per row (6).|36 / 6 = 6 rows|\n|2|How many rows of blue tulips will Jackson plant?|Divide the total number of blue tulips (24) by the number of blue tulips per row (8).|24 / 8 = 3 rows|\n|3|How many total rows of flowers will Jackson plant?|Add the number of rows of red tulips (6) to the number of rows of blue tulips (3).|6 + 3 = 9 rows|. \nTherefore, the answer is Jackson will plant 9 total rows of flowers. Example 2:  The bakers at the Beverly Hills Bakery baked 200 loaves of bread on Monday morning. They sold 93 loaves in the morning and 39 loaves in the afternoon. A grocery store returned 6 unsold loaves. How many loaves of bread did they have left? Format the response as a completion of this table.\n|step|subquestion|procedure|result|\n|:---|:----------|:--------|:-----:| {insert response #1}. \nTherefore, the answer is {insert response #2}.

Response #1

`openai/gpt-4`'s response (✅): 

|Step|Subquestion|Procedure|Result|
|:---|:----------|:--------|:-----|
|1|How many loaves of bread were sold in total?|Add the number of loaves sold in the morning (93) to the number of loaves sold in the afternoon (39).|93 + 39 = 132 loaves|
|2|How many loaves of bread were returned by the grocery store?|The grocery store returned 6 loaves of bread.|6 loaves|
|3|How many loaves of bread were left after the sales?|Subtract the total number of loaves sold (132) from the initial number of loaves baked (200).|200 - 132 = 68 loaves|
|4|How many loaves of bread did they have left after returns?|Add the number of loaves returned (6) to the number of loaves left after sales (68).|68 + 6 = 74 loaves|.

`openai/gpt-3.5`'s response (❌):

|step|subquestion|procedure|result|
|:---|:----------|:--------|:-----:|
|1|How many loaves of bread did the Beverly Hills Bakery sell?|Add the number of loaves sold in the morning (93) to the number of loaves sold in the afternoon (39).|93 + 39 = 132 loaves|
|2|How many loaves of bread were returned by the grocery store?|Subtract the number of returned loaves (6) from the total number of loaves sold (132).|132 - 6 = 126 loaves|
|3|How many loaves of bread did the bakery have left?|Subtract the number of loaves sold (132) from the total number of loaves baked (200).|200 - 132 = 68 loaves|

`tiiuae/falcon-40b-instruct`'s response (✅):

| Step |         Subquestion            |             Procedure                        | Result |
|------|-------------------------------|----------------------------------------------|--------|
|1|How many rows of red tulips will Jackson plant?|Divide the total number of red tulips (18) by the number of red tulips per row (3).|18 / 3 = 6 rows|
|2|How many rows of blue tulips will Jackson plant?|Divide the total number of blue tulips (12) by the number of blue tulips per row (4).|12 / 4 = 3 rows|
|3|How many total rows of flowers will Jackson plant?|Add the number of rows of red tulips (6) to the number of rows of blue tulips (3).|6 + 3 = 9 rows|. 

`google/flan-t5-xxl`'s response (✅):
| Step |         Subquestion            |             Procedure                        | Result |
|------|-------------------------------|----------------------------------------------|--------|
|1|How many rows of red tulips will Jackson plant?|Divide the total number of red tulips (18) by the number of red tulips per row (3).|18 / 3 = 6 rows| 
|2|How many rows of blue tulips will Jackson plant?|Divide the total number of blue tulips (12) by the number of blue tulips per row (4).|12 / 4 = 3 rows| 
|3|How many total rows of flowers will Jackson plant?|Add the number of rows of red tulips to the number of rows of blue tulips.|6 + 3 = 9 rows|


Response #2:

| model                      | correct | response             |
|----------------------|:---------:|--------------------------|
| `openai/gpt-4`               | ✅       | Beverly Hills Bakery had 74 loaves of bread left. |
| `openai/gpt-3.5`             | ❌       | Therefore, the answer is the Beverly Hills Bakery had 68 loaves of bread left. |
| `tiiuae/falcon-40b-instruct` |  ✅      | Jackson will plant 9 total rows of flowers. |
| `google/flan-t5-xxl` |    ✅    | 6 + 3 = 9 rows. Therefore, the answer is Jackson will plant 9 total rows of flowers. |






