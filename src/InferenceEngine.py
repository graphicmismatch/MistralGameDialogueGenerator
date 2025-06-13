import os
import asyncio
from dotenv import load_dotenv, find_dotenv
from mistralai import Mistral


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

    def GiveStandardPrompt(
        self, callback, userprompt: str, systemprompt: str = None, temp: float = None
    ):
        messagedict = []
        if systemprompt is not None:
            messagedict.append({"role": "system", "content": f"{systemprompt}"})
        messagedict.append({"role": "user", "content": f"{userprompt}"})
        if temp is None:
            temp = self.temp
        asyncio.run(self.StandardPromptWorker(callback, messagedict, temp))

    async def StandardPromptWorker(self, callback, messagedict, temp: float):
        res = await self.client.chat.complete_async(
            model=self.model, messages=messagedict, temperature=temp
        )
        callback(res)
