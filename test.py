from src.InferenceEngine import InferenceEngine, FSLData


# inference engine setup
ie = InferenceEngine(temp=0.1)


# Example Callback
def testingres(res):
    print(res.choices[0].message.content)


# MultiShot/FewShot Learning setup
examples = []

examples.append(
    FSLData(
        "Say Hello World in a random language.",
        "1) Language: translation",
    )
)
examples.append(
    FSLData(
        "Say Hello World in 2 random languages.",
        "1) English: smtg smtg\n2) French: smtg smtg",
    )
)


ie.GivePrompt(
    testingres,
    "Say Hello World in 12 random languages.",
    learning=examples,
)
