# Simple AI back end switcher

Provides a consistent simple interface to multiple AI LLM back ends:

Completed:
- Poe unofficial API
- OpenAI offical ChatGPT api


Todo:
- llama.cpp for your own models

## Installation

`pip install simpleaiswitcher`

## Usage

```
from simpleaiswitcher import SimpleAI
from simpleaiswitcher import AIBackEndType as BackEnd

poe_access_token = "<your poe cookie value>"
openai_access_token = "<your openai api token>"

poe = SimpleAI(BackEnd.OpenAI, poe_access_token)

chatgpt = SimpleAI(BackEnd.Poe, openai_access_token)

print(poe.reply("hello"))

print(chatgpt.reply("hello"))
```

