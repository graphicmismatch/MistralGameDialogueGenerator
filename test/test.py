from utils.InferenceEngine import InferenceEngine
from utils.PromptBuilder import PromptBuilder as pb

ie = InferenceEngine(temp=0.2)
builder = pb("characters/jarvis.json")
prompt = builder.build_prompt(
    "The player just landed on Mars and asks if it's safe to remove their helmet."
)


def testingres(res):

    print(res.choices[0].message.content)


pb.GetProfessionalGameDeveloper(
    testingres,
    ie,
    "5",
    "dark fantasy",
    "a wizarding class room",
    "",
    "",
    "",
)
