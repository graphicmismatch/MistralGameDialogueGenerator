from src.InferenceEngine import InferenceEngine
from src.PromptBuilder import PromptBuilder

ie = InferenceEngine(temp=0.2)
builder = PromptBuilder("characters/jarvis.json")
prompt = builder.build_prompt("The player just landed on Mars and asks if it's safe to remove their helmet.")

def testingres(res):
    print("Jarvis says:\n")
    print(res.choices[0].message.content)

ie.GivePrompt(
    callback=testingres,
    userprompt=prompt
)
