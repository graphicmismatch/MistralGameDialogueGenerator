import streamlit as st
from src.logic.InferenceEngine import InferenceEngine
from src.logic.PromptBuilder import PromptBuilder as pb


def display_callback(result):
    st.text(result.choices[0].message.content)


ie = InferenceEngine()

st.set_page_config(page_title="Game Dev Hub", layout="centered")
st.title("🎮 Game Development Portal")


tab1, tab2, tab3 = st.tabs(
    ["Casual Game Developer", "Professional Game Developer", "Game Reviewer"]
)

with tab1:
    st.header("👾 Casual Game Developer")
    st.info("This section is under development. Stay tuned!")


with tab2:
    st.header("🧠 Professional Game Developer")

    with st.form("prof_dev_form"):
        length = st.text_input("Dialogue Length")
        theme = st.text_input("Theme")
        setting = st.text_input("Setting")
        context = st.text_input("Context")
        characters = st.text_input("Characters")
        mood = st.text_input("Mood")

        submitted = st.form_submit_button("Submit")

        if submitted:
            pb.GetProfessionalGameDeveloper(
                callback=display_callback,
                ie=ie,
                length=length,
                theme=theme,
                setting=setting,
                context=context,
                characters=characters,
                mood=mood,
            )


with tab3:
    st.header("📝 Game Reviewer")
    st.info("This section is under development. Check back later!")
