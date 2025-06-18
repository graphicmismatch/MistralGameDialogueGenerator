import os
import asyncio
from dotenv import load_dotenv, find_dotenv
from mistralai import Mistral
from dataclasses import dataclass
from typing import *

import asyncio


import asyncio


def run_async_task(coro):
    try:
        loop = asyncio.get_event_loop()
        if loop.is_closed():
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
        return loop.run_until_complete(coro)
    except RuntimeError:
        # Fallback for cases where loop is closed or doesn't exist
        new_loop = asyncio.new_event_loop()
        asyncio.set_event_loop(new_loop)
        return new_loop.run_until_complete(coro)


@dataclass
class FSLData:
    prompt: str
    response: str


class InferenceEngine:

    def __init__(
        self,
        modelname: str = "mistral-small-2503",
        temp: float = 0.2,
    ):
        if find_dotenv() == "":
            raise FileNotFoundError(".env file not found")
        load_dotenv()
        apikey = os.getenv("MISTRAL_API_KEY")
        if apikey is None:
            raise KeyError("key MISTRAL_API_KEY not found in .env file")
        self.model = modelname
        self.client = Mistral(api_key=apikey)
        self.temp = temp

    def GivePrompt(
        self,
        callback,
        userprompt: str,
        systemprompt: str = None,
        learning: List[FSLData] = None,
        temp: float = None,
    ):
        messagedict = []
        if learning is not None:
            if systemprompt is None:
                systemprompt = ""
            systemprompt += "\n ALWAYS follow the format in the provided examples. The examples are only for formatting, the actual content of the examples is less important. DO NOT deviate from the format."
        if systemprompt is not None:
            messagedict.append({"role": "system", "content": f"{systemprompt}"})

        if learning is not None:
            n = 0
            for i in learning:
                n += 1
                t = f"Example {n}: " + i.prompt
                messagedict.append({"role": "user", "content": f"{t}"})
                messagedict.append({"role": "assistant", "content": f"{i.response}"})

        messagedict.append({"role": "user", "content": f"{userprompt}"})

        if temp is None:
            temp = self.temp
        run_async_task(self.PromptWorker(callback, messagedict, temp))

    async def PromptWorker(self, callback, messagedict, temp: float):
        res = await self.client.chat.complete_async(
            model=self.model, messages=messagedict, temperature=temp
        )
        callback(res)
