# Simple AI back end switcher

Provides a consistent simple interface to multiple AI LLM back ends:

Completed:
- Poe unofficial API
- OpenAI offical ChatGPT api


Todo:
- llama.cpp for your own models

## Installation

`pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ simpleaibackendswitcher `

## Usage

```
from simpleaiswitcher import SimpleAI
from simpleaiswitcher import AIBackEndType as BackEnd

poe_access_token = "<your poe cookie value>"
openai_access_token = "<your openai api token>"

poe = SimpleAI(BackEnd.Poe, poe_access_token)

chatgpt = SimpleAI(BackEnd.OpenAI, openai_access_token)

poe_says = poe.reply("hello")

chatgpt_says = chatgpt.reply(poe_says)

print('from poe: "', poe_says)
print('from chatgpt: "', chatgpt_says)
```

