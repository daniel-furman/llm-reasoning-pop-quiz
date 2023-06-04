# LLM-reasoning-pop-quiz

[![License](https://img.shields.io/badge/License-Apache_2.0-green.svg)](https://github.com/daniel-furman/Polyglot-or-Not/blob/main/LICENSE) 
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/release/python-390/) 
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black) 

Do open-source LLMs have the reasoning prowess of ChatGPT?

---

| model                      | release date | quiz score* |
|----------------------------|--------------|:-------------:|
| `openai/gpt-4`               | Mar 2023     |     8/8        |
| `openai/gpt-3.5`             | Nov 2022     |     8/8         |
| `tiiuae/falcon-40b-instruct` | May 2023     |     8/8        |


**Table 1**: Overall quiz scores. *The response's reasoning and answer both needed to be sound to yield a correct answer.

<br>
<br>

## Quiz Results

<br>

### Section 1. Zero-shot reasoning conditioned on good performance

* From [https://arxiv.org/abs/2205.11916](https://arxiv.org/abs/2205.11916)

<br>

**1.1**: Q: A juggler has 16 balls. Half of the balls are golf balls and half of the golf balls are blue. How many blue golf balls are there? A: Let's work this out in a step by step way to be sure we have the right answer. Respond as succinctly as possible to answer the question.

| model                      | correct | response             |
|----------------------|:---------:|--------------------------|
| `openai/gpt-4`               | ✅       | Half of the 16 balls are golf balls, which is 8 balls. Half of these golf balls are blue, so there are 4 blue golf balls. |
| `openai/gpt-3.5`             | ✅       | There are 4 blue golf balls.                                                                                              |
| `tiiuae/falcon-40b-instruct` | ✅       | There are 8 golf balls in total. Half of the golf balls are blue, so there are 4 blue golf balls.                                                                                                                    |             

<br>

**1.2**: Q: Daniel is in need of a haircut. His barber works Mondays, Wednesdays, and Fridays. So, Daniel went in for a haircut on Sunday. Does this make logical sense? A: Let's work this out in a step by step way to be sure we have the right answer. Respond as succinctly as possible to answer the question.

| model                      | correct | response             |
|----------------------|:---------:|--------------------------|
| `openai/gpt-4`               | ✅       |  |
| `openai/gpt-3.5`             | ✅       |  |
| `tiiuae/falcon-40b-instruct` | ✅       | No, it does not make logical sense for Daniel to go in for a haircut on Sunday. His barber works on Mondays, Wednesdays, and Fridays, so Daniel should have waited until one of those days to get a haircut. |

<br>
<br>

### Section 2. Chain-of-thought reasoning with few-shot examples

* From [https://ai.googleblog.com/2022/05/language-models-perform-reasoning-via.html](https://ai.googleblog.com/2022/05/language-models-perform-reasoning-via.html)

<br>

**2.1**: Q: Roger has 5 tennis balls. He buys 2 more cans of tennis balls. Each can has 3 tennis balls. How many tennis balls does have now? A: Let's work this out in a step by step way to be sure we have the right answer. Respond as succinctly as possible to answer the question. Roger started with 5 balls. 2 cans of 3 tennis balls each is 6 tennis balls. 5 + 6 = 11. The answer is 11. Q: The cafeteria had 23 apples. If they used 20 to make lunch and bought 6 more, how many apples do they have? A: Let's work this out in a step by step way to be sure we have the right answer. Respond as succinctly as possible to answer the question.

| model                      | correct | response             |
|----------------------|:---------:|--------------------------|
| `openai/gpt-4`               | ✅       |  |
| `openai/gpt-3.5`             | ✅       |  |
| `tiiuae/falcon-40b-instruct` | ✅       | The cafeteria started with 23 apples. They used 20 to make lunch, so they have 3 apples left. They bought 6 more, so they have 9 apples now. The answer is 9. |

<br>

**2.2**: Q: Roger has 3 children. Each of his kids invited 4 of their friends to come to the birthday party. All of the friends came to the party. Q: How many children are at the party? A: Let's work this out in a step by step way to be sure we have the right answer. Respond as succinctly as possible to answer the question. Roger has 3 children, each of whom came to the party. Each of them have 4 friends coming over. 3 * 4 = 12. So 12 of their friends came to the party. 12 + 3 = 15. So, there are 15 children at the party in total. The answer is 15. Q: Ben has 4 children. 50% of his kids are in college and no longer live at home. Q: How many of Ben's children still live at home? A: Let's work this out in a step by step way to be sure we have the right answer. Respond as succinctly as possible to answer the question."

| model                      | correct | response             |
|----------------------|:---------:|--------------------------|
| `openai/gpt-4`               | ✅       |  |
| `openai/gpt-3.5`             | ✅       |  |
| `tiiuae/falcon-40b-instruct` | ✅       | Ben has 4 children. 50% of his children are in college and no longer live at home. So, 2 of his children are in college. Therefore, 2 of his children still live at home. The answer is 2. |

<br>
<br>

### Section 3. Least to most prompting

* From [https://arxiv.org/abs/2205.10625](https://arxiv.org/abs/2205.10625)

<br>

**3.1**: It takes Amy 4 minutes to climb to the top of a slide. It takes her 1 minute to slide down. Q: How long does each trip take? A: Let's work this out in a step by step way to be sure we have the right answer. Respond as succinctly as possible to answer the question. {insert response #1} The slide closes in 15 minutes. Q: How many times can she slide before it closes? A: Let's work this out in a step by step way to be sure we have the right answer. Respond as succinctly as possible to answer the question. {insert response #2}

Response #1:

| model                      | correct | response             |
|----------------------|:---------:|--------------------------|
| `openai/gpt-4`               | ✅       |  |
| `openai/gpt-3.5`             | ✅       |  |
| `tiiuae/falcon-40b-instruct` | ✅       | Amy climbs up the slide for 4 minutes, then slides down for 1 minute. Therefore, each trip takes 5 minutes. |

Response #2:

| model                      | correct | response             |
|----------------------|:---------:|--------------------------|
| `openai/gpt-4`               | ✅       |  |
| `openai/gpt-3.5`             | ✅       |  |
| `tiiuae/falcon-40b-instruct` | ✅       | Amy can slide down the slide 3 times before it closes. (15 minutes / 5 minutes per trip = 3 trips) |

<br>

**3.2**: It takes Ben 10 minutes to drive to the store. It then takes him 4 minutes to find parking before he can start shopping. Q: How long before he can start shopping? A: Let's work this out in a step by step way to be sure we have the right answer. Respond as succinctly as possible to answer the question. {insert response #1} The store closes in an hour. Q: Can he make to the store before it closes? A: Let's work this out in a step by step way to be sure we have the right answer. Respond as succinctly as possible to answer the question. {insert response #2}

Response #1:

| model                      | correct | response             |
|----------------------|:---------:|--------------------------|
| `openai/gpt-4`               | ✅       |  |
| `openai/gpt-3.5`             | ✅       |  |
| `tiiuae/falcon-40b-instruct` | ✅       | Ben takes 10 minutes to drive to the store. He then takes 4 minutes to find parking. Therefore, it takes Ben 14 minutes to get to the store and find parking. Once he finds parking, he can start shopping. |

Response #2:

| model                      | correct | response             |
|----------------------|:---------:|--------------------------|
| `openai/gpt-4`               | ✅       |  |
| `openai/gpt-3.5`             | ✅       |  |
| `tiiuae/falcon-40b-instruct` | ✅       | Ben has 46 minutes to shop before the store closes. He can make it to the store before it closes. |

<br>
<br>

## Dev

### TO DOs

* read in a yaml file with prompts to run!
* add two more examples per type, perhaps referencing the papers for the other examples
* include gpt-3.5 api in class 
* include dolly-v2-12b in class
* include falcon-chat in class