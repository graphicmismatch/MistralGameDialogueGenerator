import streamlit as st
from src.InferenceEngine import InferenceEngine

st.write("Hello World")

ie = InferenceEngine()


def testingres(res):
    print(res.choices[0].message.content)


ie.GiveStandardPrompt(testingres, "Say Hello World in 3 random languages.", temp=1)
