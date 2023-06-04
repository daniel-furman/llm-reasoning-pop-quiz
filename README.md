# LLM-reasoning-pop-quiz

[![License](https://img.shields.io/badge/License-Apache_2.0-green.svg)](https://github.com/daniel-furman/Polyglot-or-Not/blob/main/LICENSE) 
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/release/python-390/) 
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black) 

Do open-source LLMs have the reasoning prowess of ChatGPT?

---

| model                      | release date | quiz score* |
|----------------------------|--------------|-------------|
| openai/gpt-4               | Mar 2023     |             |
| openai/gpt-3.5             | Nov 2022     |             |
| tiiuae/falcon-40b-instruct | May 2023     |             |


**Table 1**: Overall quiz scores. *How quiz scores were evaluated... insert.

## Question generations

### Zero-shot reasoning conditioned on good performance

| model                      | prompt / generations                                                                                                                                                                                                                                                                  |
|----------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| question 1                 | prompt: A juggler has 16 balls. Half of the balls are golf balls and half of the golf balls are blue. How many blue golf balls are there? A: Let's work this out in a step by step way to be sure we have the right answer. Respond as succinctly as possible to answer the question. |
| openai/gpt-4 (✅)           | Half of the 16 balls are golf balls, which is 8 balls. Half of these golf balls are blue, so there are 4 blue golf balls.                                                                                                                                                             |
| openai/gpt-3.5 (✅)         | There are 4 blue golf balls.                                                                                                                                                                                                                                                          |
| tiiuae/falcon-40b-instruct |                                                                                                                                                                                                                                                                                       |
|                            |                                                                                                                                                                                                                                                                                       |
|                            |                                                                                                                                                                                                                                                                                       |

### TO DOs

* read in a yaml file with prompts to run!
* add two more examples per type, perhaps referencing the papers for the other examples
* add direct caching to csv in notebook, enable running chunks separately, caching
* include gpt-3.5 api in class 
* include dolly-v2-12b in class
* include falcon-chat in class
