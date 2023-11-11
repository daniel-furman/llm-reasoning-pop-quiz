# LLM-reasoning-pop-quiz

[![License](https://img.shields.io/badge/License-Apache_2.0-green.svg)](https://github.com/daniel-furman/Polyglot-or-Not/blob/main/LICENSE) 
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/release/python-390/) 
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black) 

---

## Test Leaderboard

| model   | size |	alignment | alpaca eval (win rate %)    | pop quiz score (**here**)    | test date    | 
|----------|:--------------:|--------------|:--------------:|:-------------:|:--------------:|
| `mistralai/mistral-7b-instruct-v0.1` |   7B       |    SFT   |   	-          |    7/8       |  11/11/23   |

<br>

## Questions with Answers

**NB**: Only the top performing models are shown in the responses below. See the ```notebooks``` folder for more results.

### Section 1. Zero-shot CoT reasoning

* From [https://arxiv.org/abs/2205.11916](https://arxiv.org/abs/2205.11916)

**1.1** A juggler has 16 balls. Half of the balls are golf balls and half of the golf balls are blue. How many blue golf balls are there?\nLet's respond succinctly and work this out in a step by step way to be sure we have the right answer.

| model                        |  response             | correct  |
|------------------------------|-----------------------|:---------:|
| `mistralai/mistral-7b-instruct-v0.1` | Here's how you can solve it:<br /><br />1. The juggler has 16 balls.<br />2. Half of these balls are golf balls, so there are 16 / 2 = 8 golf balls.<br />3. Half of the golf balls are blue, so there are 8 / 2 = 4 blue golf balls.<br /><br />Therefore, there are 4 blue golf balls. | ✅ |

<br>

**1.2** Daniel is in need of a haircut. His barber works Mondays, Wednesdays, and Fridays. So, Daniel went in for a haircut on Sunday. Does this make logical sense?\nLet's respond succinctly and work this out in a step by step way to be sure we have the right answer.

| model                        |  response             | correct  |
|------------------------------|-----------------------|:---------:|
| `mistralai/mistral-7b-instruct-v0.1` | No, it does not make logical sense. Here's why:<br /><br />1. The barber works only on Mondays, Wednesdays, and Fridays.<br />2. Therefore, if Daniel went in for a haircut on Sunday, he would not be able to get his hair cut because the barber was not working that day.<br />3. It seems like there might have been some confusion or misunderstanding about when the barber is available for appointments. | ✅ |

<br>

**1.3** The cafeteria had 23 apples. If they used 20 to make lunch and bought 6 more, how many apples do they have? Let's respond succinctly and work this out in a step by step way to be sure we have the right answer.

| model                        |  response             | correct  |
|------------------------------|-----------------------|:---------:|
| `mistralai/mistral-7b-instruct-v0.1` | Initially, the cafeteria had 23 apples. They used 20 of those apples to make lunch, leaving them with 3 apples. Then, they bought 6 more apples, bringing their total to 9 apples. | ✅ |

<br>

**1.4** Roger has 3 children. Each of his kids invited 4 of their friends to come to the birthday party. All of the friends came to the party. How many children are at the party? Let's respond succinctly and work this out in a step by step way to be sure we have the right answer.

| model                        |  response             | correct  |
|------------------------------|-----------------------|:---------:|
| `mistralai/mistral-7b-instruct-v0.1` | Here's how you can solve it:<br /><br />1. We know that Roger has 3 children.<br />2. Then we are told that each of his kids invited 4 friends. So, in total, there are 3 children (Roger's) + 4 friends per child = 12 friends.<br />3. The question states that all of the friends came to the party. Therefore, there are 12 friends + 3 children (Roger's) = 15 children at the party. | ✅ |


### Section 2. Least to most prompting

* From [https://arxiv.org/abs/2205.10625](https://arxiv.org/abs/2205.10625)


**2.1**: It takes Amy 4 minutes to climb to the top of a slide. It takes her 1 minute to slide down. How long does each trip take?\nLet's respond succinctly and work this out in a step by step way to be sure we have the right answer. `{insert response #1}` The slide closes in 15 minutes. How many times can she slide before it closes?\nLet's respond succinctly and work this out in a step by step way to be sure we have the right answer. `{insert response #2}`

Response #1:

| model                        | response             | correct   |
|------------------------------|----------------------|:---------:|
| `mistralai/mistral-7b-instruct-v0.1` |  Each trip takes 5 minutes. Here's how we can figure that out:<br /><br />1. We know that it takes Amy 4 minutes to climb up the slide.<br />2. Then, once she reaches the top, it takes her only 1 minute to slide back down.<br />3. Therefore, the total time for one trip (climbing up and sliding back down) is 4 + 1 = 5 minutes. | ✅ |

Response #2:

| model                        | response             | correct   |
|------------------------------|----------------------|:---------:|
| `mistralai/mistral-7b-instruct-v0.1` | The slide closes in 15 minutes. To find out how many times Amy can slide before it closes, we need to divide the total time the slide is open by the time it takes for one trip.<br /><br />1. The slide is open for 15 minutes.<br />2. Each trip takes 5 minutes.<br />3. Therefore, the number of trips Amy can make before the slide closes is 15 / 5 = 3 trips. | ✅ |
<br>

**2.2**: It takes Ben 10 minutes to drive to the store. It then takes him 4 minutes to find parking before he can start shopping. How long before he can start shopping?\nLet's respond succinctly and work this out in a step by step way to be sure we have the right answer. `{insert response #1}` The store closes in an hour. Can he make to the store before it closes?\nLet's respond succinctly and work this out in a step by step way to be sure we have the right answer. `{insert response #2}`

Response #1:

| model                        | response             | correct   |
|------------------------------|----------------------|:---------:|
| `mistralai/mistral-7b-instruct-v0.1` | Here's how we can solve this problem:<br /><br />1. We know that it takes Ben 10 minutes to drive to the store.<br />2. Once he arrives, it takes him an additional 4 minutes to find parking.<br />3. Therefore, the total time it takes for Ben to arrive at the store and find parking is 10 + 4 = 14 minutes.<br />4. Since Ben starts shopping once he finds parking, we can say that he can start shopping after 14 minutes.<br /><br />So, it takes Ben 14 minutes before he can start shopping. | ✅ |

Response #2:

| model                        | response             | correct   |
|------------------------------|----------------------|:---------:|
| `mistralai/mistral-7b-instruct-v0.1` | Yes, Ben can make it to the store before it closes. Here's how we can calculate this:<br /><br />1. The store closes in an hour, which is 60 minutes.<br />2. Ben takes 14 minutes to arrive at the store and find parking.<br />3. Therefore, Ben will have 60 - 14 = 46 minutes left to shop before the store closes.<br />4. Assuming Ben shops at a constant pace, he can cover 46 minutes of shopping time in 46 minutes.<br />5. Therefore, Ben can make it to the store before it closes.<br /><br />So, yes, Ben can make it to the store before it closes. | ✅ |

<br>

### Section 3. Tabular Chain of Thought

* From [https://arxiv.org/abs/2305.17812](https://arxiv.org/abs/2305.17812)

**3.1**: Jackson is planting tulips. He can fit 6 red tulips in a row and 8 blue tulips in a row. If Jackson buys 36 red tulips and 24 blue tulips, how many rows of flowers will he plant?\nRespond as succinctly as possible. Format the response as a completion of this table.\n|step|subquestion|procedure|result|\n|:---|:----------|:--------|:-----:|.

`mistralai/mistral-7b-instruct-v0.1` (✅): 

|step|subquestion|procedure|result|
|:---|:----------|:--------|:-----:|
|1|How many rows of red tulips can Jackson plant?|Divide the number of red tulips by the number of red tulips per row.|36 / 6 = 6 rows|
|2|How many rows of blue tulips can Jackson plant?|Divide the number of blue tulips by the number of blue tulips per row.|24 / 8 = 3 rows|
|3|What is the total number of rows that Jackson can plant?|Add the number of rows of red tulips to the number of rows of blue tulips.|6 + 3 = 9 rows|


**3.2**: The bakers at the Beverly Hills Bakery baked 200 loaves of bread on Monday morning. They sold 93 loaves in the morning and 39 loaves in the afternoon. A grocery store then returned 6 unsold loaves back to the bakery. How many loaves of bread did the bakery have left?\nRespond as succinctly as possible. Format the response as a completion of this table.\n|step|subquestion|procedure|result|\n|:---|:----------|:--------|:-----:|.


`mistralai/mistral-7b-instruct-v0.1` (❌): 

|step|subquestion|procedure|result|
|:---|:----------|:--------|:-----:|
|1|How many loaves were baked on Monday morning?|The bakery baked 200 loaves on Monday morning.|200|
|2|How many loaves were sold in the morning?|The bakery sold 93 loaves in the morning.|93|
|3|How many loaves were sold in the afternoon?|The bakery sold 39 loaves in the afternoon.|39|
|4|How many unsold loaves were returned to the bakery?|The grocery store returned 6 unsold loaves back to the bakery.|6|
|5|How many loaves of bread did the bakery have left?|Subtract the number of unsold loaves from the total number of loaves baked.|200 - 6 = 194|