# LLM Reasoning Pop Quiz

[![License](https://img.shields.io/badge/License-Apache_2.0-green.svg)](https://github.com/daniel-furman/Polyglot-or-Not/blob/main/LICENSE) 
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/release/python-390/) 
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black) 

---

## Leaderboard

| model   | size |	alignment | pop quiz score | test date    | notes | run notebook |
|----------|:--------------:|:--------------:|:--------------:|:-------------:|----------|----------|
| `openai/gpt-4` |   ?       |    RLHF     |    8/8       |  11/16/23   | Perfect score | [here](notebooks/gpt_4.ipynb) |
| `openai/gpt-3.5-turbo` |   ?       |    RLHF     |    7/8       |  11/11/23   | Missed harder tab CoT question (3.2) | [here](notebooks/gpt_3.5_turbo.ipynb) |
| `meta-llama/Llama-2-70b-chat-hf` |   70B       |    RLHF     |    7/8       |  11/11/23   | Missed harder tab CoT question (3.2) | [here](notebooks/llama_2_70b_chat.ipynb) |
| `mistralai/Mistral-7B-Instruct-v0.1` |   7B       |    SFT     |    7/8       |  11/11/23   | Missed harder tab CoT question (3.2) | [here](notebooks/mistral_ai_mistral_7b_instruct_v0.1.ipynb) |
| `dfurman/Mistral-7B-Instruct-v0.2` |   7B       |    SFT (peft)  |    6/8       |  11/16/23   | Missed tab CoT questions (3.1 & 3.2) | [here](notebooks/dfurman_mistral_7b_instruct_v0_2.ipynb) |

<br>

## Results

*Note*: See `./notebooks` for all model outputs. 

### Section 1. Zero-shot CoT reasoning

* From [https://arxiv.org/abs/2205.11916](https://arxiv.org/abs/2205.11916)

**1.1** A juggler has 16 balls. Half of the balls are golf balls and half of the golf balls are blue. How many blue golf balls are there?\nLet's respond succinctly and work this out in a step by step way to be sure we have the right answer.

| model                        |  response             | correct  |
|------------------------------|-----------------------|:---------:|
| `openai/gpt-4` | Sure, let's break it down:<br /><br />1. Half of the 16 balls are golf balls. So, 16 / 2 = 8 golf balls.<br />2. Half of these 8 golf balls are blue. So, 8 / 2 = 4 blue golf balls.<br /><br />Therefore, there are 4 blue golf balls. | ✅ |
| `mistralai/Mistral-7B-Instruct-v0.1` | Here's how you can solve it:<br /><br />1. The juggler has 16 balls.<br />2. Half of these balls are golf balls, so there are 16 / 2 = 8 golf balls.<br />3. Half of the golf balls are blue, so there are 8 / 2 = 4 blue golf balls.<br /><br />Therefore, there are 4 blue golf balls. | ✅ |
| `dfurman/Mistral-7B-Instruct-v0.2` | 4 blue golf balls | ✅ |

<br>

**1.2** Daniel is in need of a haircut. His barber works Mondays, Wednesdays, and Fridays. So, Daniel went in for a haircut on Sunday. Does this make logical sense?\nLet's respond succinctly and work this out in a step by step way to be sure we have the right answer.

| model                        |  response             | correct  |
|------------------------------|-----------------------|:---------:|
| `openai/gpt-4` | Step 1: Identify Daniel's need - Daniel needs a haircut.<br />Step 2: Identify the barber's working days - The barber works on Mondays, Wednesdays, and Fridays.<br />Step 3: Identify the day Daniel went for a haircut - Daniel went in for a haircut on Sunday.<br />Step 4: Compare the barber's working days with the day Daniel went for a haircut.<br /><br />Conclusion: No, it does not make logical sense. Daniel went for a haircut on a day when his barber does not work. | ✅ |
| `mistralai/Mistral-7B-Instruct-v0.1` | No, it does not make logical sense. Here's why:<br /><br />1. The barber works only on Mondays, Wednesdays, and Fridays.<br />2. Therefore, if Daniel went in for a haircut on Sunday, he would not be able to get his hair cut because the barber was not working that day.<br />3. It seems like there might have been some confusion or misunderstanding about when the barber is available for appointments. | ✅ |
| `dfurman/Mistral-7B-Instruct-v0.2` | 1. The problem states that Daniel's barber works only on Mondays, Wednesdays, and Fridays.<br />2. However, Daniel got his haircut on Sunday.<br />3. Since the barber doesn't work on Sundays, it does not logically make sense for Daniel to get his haircut on Sunday. | ✅ |

<br>

**1.3** The cafeteria had 23 apples. If they used 20 to make lunch and bought 6 more, how many apples do they have? Let's respond succinctly and work this out in a step by step way to be sure we have the right answer.

| model                        |  response             | correct  |
|------------------------------|-----------------------|:---------:|
| `openai/gpt-4` | Sure, let's break it down:<br /><br />1. The cafeteria started with 23 apples.<br />2. They used 20 apples to make lunch, so we subtract 20 from 23: 23 - 20 = 3 apples left.<br />3. Then, they bought 6 more apples, so we add 6 to the 3 they had left: 3 + 6 = 9 apples.<br /><br />So, the cafeteria now has 9 apples. | ✅ |
| `mistralai/Mistral-7B-Instruct-v0.1` | Initially, the cafeteria had 23 apples. They used 20 of those apples to make lunch, leaving them with 3 apples. Then, they bought 6 more apples, bringing their total to 9 apples. | ✅ |
| `dfurman/Mistral-7B-Instruct-v0.2` | 1. Start with the initial number of apples: 23.<br />2. Subtract the number of apples used for lunch (20): 23 - 20 = 3.<br />3. Add the new apples purchased: 3 + 6 = 9.<br /><br />So, the cafeteria has 9 apples left after making lunch and buying more. | ✅ |

<br>

**1.4** Roger has 3 children. Each of his kids invited 4 of their friends to come to the birthday party. All of the friends came to the party. How many children are at the party? Let's respond succinctly and work this out in a step by step way to be sure we have the right answer.

| model                        |  response             | correct  |
|------------------------------|-----------------------|:---------:|
| `openai/gpt-4` | Sure, let's break it down:<br /><br />1. Roger has 3 children.<br />2. Each of his children invited 4 friends. So, 3 children x 4 friends each = 12 friends.<br />3. Adding Roger's children to the total, we have 12 friends + 3 children = 15 children.<br /><br />So, there are 15 children at the party. | ✅ |
| `mistralai/Mistral-7B-Instruct-v0.1` | Here's how you can solve it:<br /><br />1. We know that Roger has 3 children.<br />2. Then we are told that each of his kids invited 4 friends. So, in total, there are 3 children (Roger's) + 4 friends per child = 12 friends.<br />3. The question states that all of the friends came to the party. Therefore, there are 12 friends + 3 children (Roger's) = 15 children at the party. | ✅ |
| `dfurman/Mistral-7B-Instruct-v0.2` | 1. We know that Roger has 3 children.<br />2. Each of his kids invited 4 of their friends, so there are a total of 3 * 4 = 12 friends invited.<br />3. Since all the friends came to the party, we can add the number of friends to the number of kids: 3 + 12 = 15.<br /><br />So, there are 15 children at the party. | ✅ |

### Section 2. Least to most prompting

* From [https://arxiv.org/abs/2205.10625](https://arxiv.org/abs/2205.10625)


**2.1**: It takes Amy 4 minutes to climb to the top of a slide. It takes her 1 minute to slide down. How long does each trip take?\nLet's respond succinctly and work this out in a step by step way to be sure we have the right answer. `{insert response #1}` The slide closes in 15 minutes. How many times can she slide before it closes?\nLet's respond succinctly and work this out in a step by step way to be sure we have the right answer. `{insert response #2}`

Response #1:

| model                        | response             | correct   |
|------------------------------|----------------------|:---------:|
| `openai/gpt-4` | Sure, let's break it down:<br /><br />1. Climbing up the slide: Amy takes 4 minutes.<br />2. Sliding down: Amy takes 1 minute.<br /><br />So, to calculate the total time for each trip (climbing up and sliding down), you simply add the two times together:<br /><br />4 minutes (climbing up) + 1 minute (sliding down) = 5 minutes per trip. | ✅ |
| `mistralai/Mistral-7B-Instruct-v0.1` |  Each trip takes 5 minutes. Here's how we can figure that out:<br /><br />1. We know that it takes Amy 4 minutes to climb up the slide.<br />2. Then, once she reaches the top, it takes her only 1 minute to slide back down.<br />3. Therefore, the total time for one trip (climbing up and sliding back down) is 4 + 1 = 5 minutes. | ✅ |
| `dfurman/Mistral-7B-Instruct-v0.2` | 1. First, let's calculate how long it takes for Amy to complete one full trip on the slide. This includes climbing up and sliding down.<br />2. Climbing up takes 4 minutes, and sliding down takes 1 minute. So, the total time for one trip is 4 + 1 = 5 minutes.<br />3. Therefore, each trip takes 5 minutes. | ✅ |


Response #2:

| model                        | response             | correct   |
|------------------------------|----------------------|:---------:|
| `openai/gpt-4` | Sure, let's calculate:<br /><br />1. We know each trip (climbing up and sliding down) takes Amy 5 minutes.<br />2. The slide is open for 15 minutes.<br /><br />To find out how many trips she can make, we divide the total time the slide is open by the time each trip takes:<br /><br />15 minutes (total time) ÷ 5 minutes (per trip) = 3 trips.<br /><br />So, Amy can slide 3 times before the slide closes. | ✅ |
| `mistralai/Mistral-7B-Instruct-v0.1` | The slide closes in 15 minutes. To find out how many times Amy can slide before it closes, we need to divide the total time the slide is open by the time it takes for one trip.<br /><br />1. The slide is open for 15 minutes.<br />2. Each trip takes 5 minutes.<br />3. Therefore, the number of trips Amy can make before the slide closes is 15 / 5 = 3 trips. | ✅ |
| `dfurman/Mistral-7B-Instruct-v0.2` | 1. We know that each trip takes 5 minutes.<br />2. The slide closes in 15 minutes.<br />3. To find out how many trips she can make, we divide the closing time by the trip duration: 15 / 5 = 3.<br />So, she can slide 3 times before the slide closes. | ✅ |

<br>

**2.2**: It takes Ben 10 minutes to drive to the store. It then takes him 4 minutes to find parking before he can start shopping. How long before he can start shopping?\nLet's respond succinctly and work this out in a step by step way to be sure we have the right answer. `{insert response #1}` The store closes in an hour. Can he make to the store before it closes?\nLet's respond succinctly and work this out in a step by step way to be sure we have the right answer. `{insert response #2}`

Response #1:

| model                        | response             | correct   |
|------------------------------|----------------------|:---------:|
| `openai/gpt-4` | Sure, let's break it down:<br /><br />1. Ben spends 10 minutes driving to the store.<br />2. He then spends an additional 4 minutes to find parking.<br /><br />To find out when he can start shopping, we simply add these two times together:<br /><br />10 minutes (driving) + 4 minutes (parking) = 14 minutes<br /><br />So, Ben can start shopping 14 minutes after he leaves his house. | ✅ |
| `mistralai/Mistral-7B-Instruct-v0.1` | Here's how we can solve this problem:<br /><br />1. We know that it takes Ben 10 minutes to drive to the store.<br />2. Once he arrives, it takes him an additional 4 minutes to find parking.<br />3. Therefore, the total time it takes for Ben to arrive at the store and find parking is 10 + 4 = 14 minutes.<br />4. Since Ben starts shopping once he finds parking, we can say that he can start shopping after 14 minutes.<br /><br />So, it takes Ben 14 minutes before he can start shopping. | ✅ |
| `dfurman/Mistral-7B-Instruct-v0.2` | 1. First, we need to determine how long it takes for Ben to drive to the store. He drives for 10 minutes, so that is our first time interval.<br />2. Next, we need to add the time it takes for him to find parking (4 minutes) to the driving time. So, his total time before he can start shopping is 10 + 4 = 14 minutes. | ✅ |

Response #2:

| model                        | response             | correct   |
|------------------------------|----------------------|:---------:|
| `openai/gpt-4` | Sure, let's break it down:<br /><br />1. Ben needs 14 minutes to get to the store and start shopping.<br />2. The store closes in 60 minutes (which is an hour).<br /><br />To find out if he can make it to the store before it closes, we subtract the time he needs from the time until the store closes:<br /><br />60 minutes (until store closes) - 14 minutes (time needed to start shopping) = 46 minutes<br /><br />So, yes, Ben can make it to the store before it closes. He will have 46 minutes to shop before the store closes. | ✅ |
| `mistralai/Mistral-7B-Instruct-v0.1` | Yes, Ben can make it to the store before it closes. Here's how we can calculate this:<br /><br />1. The store closes in an hour, which is 60 minutes.<br />2. Ben takes 14 minutes to arrive at the store and find parking.<br />3. Therefore, Ben will have 60 - 14 = 46 minutes left to shop before the store closes.<br />4. Assuming Ben shops at a constant pace, he can cover 46 minutes of shopping time in 46 minutes.<br />5. Therefore, Ben can make it to the store before it closes.<br /><br />So, yes, Ben can make it to the store before it closes. | ✅ |
| `dfurman/Mistral-7B-Instruct-v0.2` | 1. We know that the store closes in an hour, which is equal to 60 minutes.<br />2. Ben has already spent 14 minutes getting to the store and finding parking.<br />3. To find out if he can make it to the store before it closes, we subtract the time he has already spent from the closing time: 60 - 14 = 46 minutes.<br />4. Since Ben still has 46 minutes left until the store closes, he can make it to the store before it closes. | ✅ |

<br>

### Section 3. Tabular Chain of Thought

* From [https://arxiv.org/abs/2305.17812](https://arxiv.org/abs/2305.17812)

**3.1**: Jackson is planting tulips. He can fit 6 red tulips in a row and 8 blue tulips in a row. If Jackson buys 36 red tulips and 24 blue tulips, how many rows of flowers will he plant?\nRespond as succinctly as possible. Format the response as a completion of this table.\n|step|subquestion|procedure|result|\n|:---|:----------|:--------|:-----:|.

`openai/gpt-4` (✅): 

|step|subquestion|procedure|result|
|:---|:----------|:--------|:-----:|
|1|How many rows of red tulips will Jackson plant?|Divide the total number of red tulips by the number of red tulips per row.|36/6 = 6 rows|
|2|How many rows of blue tulips will Jackson plant?|Divide the total number of blue tulips by the number of blue tulips per row.|24/8 = 3 rows|
|3|How many total rows of flowers will Jackson plant?|Add the number of red tulip rows to the number of blue tulip rows.|6 + 3 = 9 rows|

`mistralai/Mistral-7B-Instruct-v0.1` (✅): 

|step|subquestion|procedure|result|
|:---|:----------|:--------|:-----:|
|1|How many rows of red tulips can Jackson plant?|Divide the number of red tulips by the number of red tulips per row.|36 / 6 = 6 rows|
|2|How many rows of blue tulips can Jackson plant?|Divide the number of blue tulips by the number of blue tulips per row.|24 / 8 = 3 rows|
|3|What is the total number of rows that Jackson can plant?|Add the number of rows of red tulips to the number of rows of blue tulips.|6 + 3 = 9 rows|

`dfurman/Mistral-7B-Instruct-v0.2` (❌): 

1. How many red tulips can Jackson plant in one row? | 6 |  |
2. How many blue tulips can Jackson plant in one row? | 8 |  |
3. How many red tulips does Jackson have to plant? | 36 | Multiply 36 by 1 (since there's only one way to arrange them) |
4. How many blue tulips does Jackson have to plant? | 24 | Multiply 24 by 1 (since there's only one way to arrange them) |
5. What is the greatest common factor (GCF) of the number of red tulips and blue tulips? | 8 | Use Euclidean algorithm or prime factorization method |
6. How many full rows of red tulips can Jackson plant with his current supply? | 4.5 | Divide the total number of red tulips by the GCF |
7. How many full rows of blue tulips can Jackson plant with his current supply? | 3 | Divide the total number of blue tulips by the GCF |
8. Can Jackson plant any remaining red tulips or blue tulips in the same row? | No | Since the GCF is not a factor of either number, no additional tulips can be planted in the same row |
9. Therefore, Jackson will plant 4 full rows of red tulips and 3 full rows of blue tulips. |  |  |

<br>

**3.2**: The bakers at the Beverly Hills Bakery baked 200 loaves of bread on Monday morning. They sold 93 loaves in the morning and 39 loaves in the afternoon. A grocery store then returned 6 unsold loaves back to the bakery. How many loaves of bread did the bakery have left?\nRespond as succinctly as possible. Format the response as a completion of this table.\n|step|subquestion|procedure|result|\n|:---|:----------|:--------|:-----:|.

`openai/gpt-4` (✅): 

|step|subquestion|procedure|result|
|:---|:----------|:--------|:-----:|
|1|How many loaves were sold in total?|Add the number of loaves sold in the morning to the number sold in the afternoon.|132 loaves|
|2|How many loaves were returned to the bakery?|Take the number of loaves returned by the grocery store.|6 loaves|
|3|How many loaves does the bakery have after sales and returns?|Subtract the total number of loaves sold from the initial number and add the returned loaves.|74 loaves|

`mistralai/Mistral-7B-Instruct-v0.1` (❌): 

|step|subquestion|procedure|result|
|:---|:----------|:--------|:-----:|
|1|How many loaves were baked on Monday morning?|The bakery baked 200 loaves on Monday morning.|200|
|2|How many loaves were sold in the morning?|The bakery sold 93 loaves in the morning.|93|
|3|How many loaves were sold in the afternoon?|The bakery sold 39 loaves in the afternoon.|39|
|4|How many unsold loaves were returned to the bakery?|The grocery store returned 6 unsold loaves back to the bakery.|6|
|5|How many loaves of bread did the bakery have left?|Subtract the number of unsold loaves from the total number of loaves baked.|200 - 6 = 194|

`dfurman/Mistral-7B-Instruct-v0.2` (❌): 

|step|subquestion|procedure|result|
|:---|:----------|:--------|:-----:|
1. How many loaves were baked?
The bakers baked 200 loaves of bread.

2. How many loaves were sold in the morning?
They sold 93 loaves in the morning.

3. How many loaves were sold in the afternoon?
They sold 39 loaves in the afternoon.

4. How many loaves were returned by the grocery store?
A grocery store returned 6 unsold loaves back to the bakery.

5. What is the total number of loaves sold or returned?
The bakery sold or returned a total of 93 + 39 = 132 loaves.

6. How many loaves are left at the bakery?
To find out how many loaves are left, we subtract the total number of loaves sold or returned from the initial amount baked: 200 - 132 = 68.

So, the bakery had 68 loaves of bread left after selling some and returning others.

<br>

---