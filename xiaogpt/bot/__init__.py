from __future__ import annotations

from xiaogpt.bot.base_bot import BaseBot
from xiaogpt.bot.chatgptapi_bot import ChatGPTBot
from xiaogpt.bot.gpt3_bot import GPT3Bot
from xiaogpt.bot.newbing_bot import NewBingBot
from xiaogpt.bot.glm_bot import GLMBot
from xiaogpt.bot.bard_bot import BardBot
from xiaogpt.bot.langchain_bot import LangChainBot
from xiaogpt.bot.ernie4_bot import Ernie4Bot  # add by yx
from xiaogpt.config import Config


BOTS: dict[str, type[BaseBot]] = {
    "gpt3": GPT3Bot,
    "newbing": NewBingBot,
    "chatgptapi": ChatGPTBot,
    "glm": GLMBot,
    "bard": BardBot,
    "langchain": LangChainBot,
    "ernie4":  Ernie4Bot # add by yx
}


def get_bot(config: Config) -> BaseBot:
    try:
        return BOTS[config.bot].from_config(config)
    except KeyError:
        raise ValueError(f"Unsupported bot {config.bot}, must be one of {list(BOTS)}")


__all__ = [
    "GPT3Bot",
    "ChatGPTBot",
    "NewBingBot",
    "GLMBot",
    "BardBot",
    "get_bot",
    "LangChainBot",
    "Ernie4Bot" # add by yx
]
