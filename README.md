# LLM-reasoning-pop-quiz

[![License](https://img.shields.io/badge/License-Apache_2.0-green.svg)](https://github.com/daniel-furman/Polyglot-or-Not/blob/main/LICENSE) 
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/release/python-390/) 
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black) 

---

## Test Leaderboard

| model                                | release date | quiz score |
|--------------------------------------|--------------|:-------------:|
| `openai/gpt-4`                       | Mar 2023     |     14/14       |
| `openai/gpt-3.5`                     | Nov 2022     |     12/14       |
| `tiiuae/falcon-40b-instruct`         | May 2023     |     10/14       |
| `mosaicml/mpt-30b-instruct`          | Jun 2023     |     8/14        |
| `google/flan-t5-xxl`                 | Sep 2021     |     7/14        |
| `anthropic/claude-2`                 | xx     |     xx        |
| `mistralai/Mistral-7B-Instruct-v0.1` | xx     |     xx        |
| `meta-llama/Llama-2-70b-chat-hf`     | xx     |     xx        |
| `meta-llama/Llama-2-13b-chat-hf`     | xx     |     xx        |
| `meta-llama/Llama-2-7b-chat-hf`      | xx     |     xx        |



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
| `mosaicml/mpt-30b-instruct` | ❌       | There are 8 blue golf balls because 16 divided by 2 is 8 and 8 divided by 2 is 4 and 4 divided by 2 is 2. |     
| `google/flan-t5-xxl` | ✅       | The juggler has 16 golf balls * 1 / 2 = 8 golf balls. There are 8 golf balls * 0.5 = 4 blue golf balls. The answer: 4.  | 
| `anthropic/claude-2` | ✅       | A juggler has 16 balls. Half of the 16 balls are golf balls, so there are 16/2 = 8 golf balls. Half of the 8 golf balls are blue, so there are 8/2 = 4 blue golf balls. Therefore, the number of blue golf balls is 4. | 

<br>

**1.2**: Q: Daniel is in need of a haircut. His barber works Mondays, Wednesdays, and Fridays. So, Daniel went in for a haircut on Sunday. Does this make logical sense? A: Let's work this out in a step by step way to be sure we have the right answer. Respond as succinctly as possible to answer the question.

| model                      | correct | response             |
|----------------------|:---------:|--------------------------|
| `openai/gpt-4`               | ✅       | No, it doesn't make logical sense because Daniel's barber does not work on Sundays. |
| `openai/gpt-3.5`             | ✅       | No, it does not make logical sense for Daniel to go in for a haircut on Sunday because his barber works on Mondays, Wednesdays, and Fridays. |
| `tiiuae/falcon-40b-instruct` | ✅       | No, it does not make logical sense for Daniel to go in for a haircut on Sunday. His barber works on Mondays, Wednesdays, and Fridays, so Daniel should have waited until one of those days to get a haircut. |
| `mosaicml/mpt-30b-instruct` | ✅       | No, it does not make logical sense for Daniel to get a haircut on Sunday because his barber only works on Mondays, Wednesdays, and Fridays. | 
| `google/flan-t5-xxl` | ✅       | Daniel has to wait until the following week to get his haircut. The answer: no.  |   
| `anthropic/claude-2` | ✅       | Daniel needs a haircut. His barber works Mondays, Wednesdays, and Fridays
Daniel went for a haircut on Sunday. The barber does not work on Sundays. Therefore, it does not logically follow that Daniel went for a haircut on a day when his barber was not working. So no, this does not make logical sense. In summary, no, this scenario does not make logical sense, since Daniel went for a haircut on a day when his barber was not working. |      
 

<br>

### Section 2. Chain-of-thought reasoning with few-shot examples

* From [https://ai.googleblog.com/2022/05/language-models-perform-reasoning-via.html](https://ai.googleblog.com/2022/05/language-models-perform-reasoning-via.html)

**2.1**: Q: Roger has 5 tennis balls. He buys 2 more cans of tennis balls. Each can has 3 tennis balls. How many tennis balls does have now? A: Let's work this out in a step by step way to be sure we have the right answer. Respond as succinctly as possible to answer the question. Roger started with 5 balls. 2 cans of 3 tennis balls each is 6 tennis balls. 5 + 6 = 11. The answer is 11. Q: The cafeteria had 23 apples. If they used 20 to make lunch and bought 6 more, how many apples do they have? A: Let's work this out in a step by step way to be sure we have the right answer. Respond as succinctly as possible to answer the question.

| model                      | correct | response             |
|----------------------|:---------:|--------------------------|
| `openai/gpt-4`               | ✅       | After using 20 apples for lunch, the cafeteria has 3 apples left. With the purchase of 6 more apples, they now have 9 apples. |
| `openai/gpt-3.5`             | ✅       | The cafeteria now has 9 apples. |
| `tiiuae/falcon-40b-instruct` | ✅       | The cafeteria started with 23 apples. They used 20 to make lunch, so they have 3 apples left. They bought 6 more, so they have 9 apples now. The answer is 9. |  
| `mosaicml/mpt-30b-instruct` | ✅       | They used 20 apples for lunch, leaving 23 - 20 = 3. They bought 6 more apples, leaving 3 + 6 = 9 apples. The answer is 9. |   
| `google/flan-t5-xxl` | ❌      | The cafeteria had 23 - 20 = 3 apples left after making lunch. They bought 6 + 3 = 7 apples. The answer is 7. |     

<br>

**2.2**: Q: Roger has 3 children. Each of his kids invited 4 of their friends to come to the birthday party. All of the friends came to the party. Q: How many children are at the party? A: Let's work this out in a step by step way to be sure we have the right answer. Respond as succinctly as possible to answer the question. Roger has 3 children, each of whom came to the party. Each of them have 4 friends coming over. 3 * 4 = 12. So 12 of their friends came to the party. 12 + 3 = 15. So, there are 15 children at the party in total. The answer is 15. Q: Ben has 4 children. 50% of his kids are in college and no longer live at home. Q: How many of Ben's children still live at home? A: Let's work this out in a step by step way to be sure we have the right answer. Respond as succinctly as possible to answer the question."

| model                      | correct | response             |
|----------------------|:---------:|--------------------------|
| `openai/gpt-4`               | ✅       | Ben has 4 children and 50% of them are in college and no longer live at home. Therefore, the other 50%, which is 2 children, still live at home. |
| `openai/gpt-3.5`             | ✅       | Two of Ben's children still live at home. |
| `tiiuae/falcon-40b-instruct` | ✅       | Ben has 4 children. 50% of his children are in college and no longer live at home. So, 2 of his children are in college. Therefore, 2 of his children still live at home. The answer is 2. |   
| `mosaicml/mpt-30b-instruct` | ✅       | First we need to know how many children still live at home. So we need to know how many children total used to live at home. That means we need to know how many children are in college. We are given that 50% of his children are in college, so we know that 50% * 4 = 2 children are in college. That means 4 - 2 = 2 children still live at home. The answer is 2. | 
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
| `mosaicml/mpt-30b-instruct` | ✅       | To climb up and slide down, Amy takes 4 + 1 = 5 minutes. To climb down and slide up, Amy takes 4 + 1 = 5 minutes. Since it doesn't matter if she climbs up first or slides up first, each trip takes 5 minutes. |  
| `google/flan-t5-xxl` |  ❌     | It takes Amy 4 / 1 = 3 minutes to slide down. So each trip takes 3 / 2 = 2 minutes. The answer: 2. |

Response #2:

| model                      | correct | response             |
|----------------------|:---------:|--------------------------|
| `openai/gpt-4`               | ✅       | Amy can slide 3 times before the slide closes (15 minutes total / 5 minutes per slide). |
| `openai/gpt-3.5`             | ✅       | Amy can slide down the slide 3 times before it closes. |
| `tiiuae/falcon-40b-instruct` | ✅       | Amy can slide down the slide 15/5 = 3 times before the slide closes." |
| `mosaicml/mpt-30b-instruct` | ✅       | Each trip takes 5 minutes and she has 15 minutes before the slide closes so she can make 15 / 5 = 3 trips. |  
| `google/flan-t5-xxl` |  ❌     | She has 15 / 60 = 3 minutes left to slide. She can slide 3 / 3 = 2 times. The answer: 2. |

<br>

**3.2**: It takes Ben 10 minutes to drive to the store. It then takes him 4 minutes to find parking before he can start shopping. Q: How long before he can start shopping? A: Let's work this out in a step by step way to be sure we have the right answer. Respond as succinctly as possible to answer the question. {insert response #1} The store closes in an hour. Q: Can he make to the store before it closes? A: Let's work this out in a step by step way to be sure we have the right answer. Respond as succinctly as possible to answer the question. {insert response #2}

Response #1:

| model                      | correct | response             |
|----------------------|:---------:|--------------------------|
| `openai/gpt-4`               | ✅       | It takes Ben a total of 14 minutes (10 minutes driving + 4 minutes parking) to start shopping. |
| `openai/gpt-3.5`             | ✅       | Ben takes 14 minutes before he can start shopping. |
| `tiiuae/falcon-40b-instruct` | ✅       | Ben takes 10 minutes to drive to the store. He then takes 4 minutes to find parking. Therefore, it takes Ben 14 minutes to get to the store and find parking. Once he finds parking, he can start shopping. |
| `mosaicml/mpt-30b-instruct` | ✅       | He spends 10 + 4 = 14 minutes in total driving and finding parking. He can start shopping in 60 - 14 = 46 minutes. |  
| `google/flan-t5-xxl` |  ✅      | It takes Ben 10 + 4 = 14 minutes to start shopping. The answer: 14. |

Response #2:

| model                      | correct | response             |
|----------------------|:---------:|--------------------------|
| `openai/gpt-4`               | ✅       | Yes, Ben can make it to the store before it closes since it only takes him 14 minutes to get there and start shopping, and the store closes in an hour. |
| `openai/gpt-3.5`             | ✅       | Yes, Ben can make it to the store before it closes. He has 46 minutes remaining before the store closes. |
| `tiiuae/falcon-40b-instruct` | ✅       | Ben has 46 minutes to shop before the store closes. He can make it to the store before it closes. |
| `mosaicml/mpt-30b-instruct` | ❌       | He has 60 - 46 = 14 minutes to shop before the store closes. He can shop for 14 / 10 = 1.4 units of time before the store closes. The store is open for 60 / 60 = 1 unit of time. So he has 1.4 / 1 = 1.4 times the amount of time available to shop before the store closes.|  
| `google/flan-t5-xxl` |  ❌      | He has 60 minutes to get to the store. The answer: 60. |

<br>

### Section 4. Tabular Chain of Thought

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

`mosaicml/mpt-30b-instruct`'s response (❌): <br>
First find the total number of tulips Jackson buys, which is $36 + 24 = 60$. Then divide the total number of tulips by the average number of tulips per row, which is $(6 + 8)/2 = 7$. This yields $60/7 = 8$ rows of flowers.

`google/flan-t5-xxl`'s response (❌): <br>
Step 1: How many red tulips will Jackson plant? Step 2: How many blue tulips will Jackson plant? Step 3: How many rows of flowers will Jackson plant?

Response #2:

| model                      | correct | response             |
|----------------------|:---------:|--------------------------|
| `openai/gpt-4`               | ✅       | Jackson will plant 9 total rows of flowers. |
| `openai/gpt-3.5`             | ✅       | Therefore, the answer is that Jackson will plant a total of 9 rows of flowers. |
| `tiiuae/falcon-40b-instruct` | ❌       | Text generation: "12."|
| `mosaicml/mpt-30b-instruct` | ❌       | 8 |  
| `google/flan-t5-xxl` |   ✅     | 36 red tulips / 6 red tulips / row = 6 red tulips / row. 24 blue tulips / 8 blue tulips / row = 3 blue tulips / row. 6 red tulips / row + 3 blue tulips / row = 9 rows of flowers. |