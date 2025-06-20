import streamlit as st
from utils.InferenceEngine import InferenceEngine
from utils.PromptBuilder import PromptBuilder as pb


def display_callback(result):
    st.markdown(result.choices[0].message.content)


ie = InferenceEngine()

st.set_page_config(page_title="Game Dialogue Hub", layout="centered")
st.title("🎮 Game Dialogue Hub")


tab1, tab2, tab3 = st.tabs(
    ["Casual Game Developer", "Professional Game Developer", "Game Reviewer"]
)

with tab1:
    st.header("👻 Casual Game Developer")
    st.subheader("Real-Time Dialogue Generator")

    with st.form("cas_dev_form"):
        char_name = st.text_input("Character Name")
        theme = st.text_input("Theme")
        mood = st.text_input("Mood")
        situation = st.text_area("What's happening in the game?")
        submitted = st.form_submit_button("Submit")
        if submitted:
            pb.BuildCasualPrompt(
                callback=display_callback,
                ie=ie,
                character=char_name,
                theme=theme,
                mood=mood,
                situation=situation,
            )

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
    st.header("📝 Game Reviewer & Influencer")
    st.subheader("Customized Content")

    with st.form("reviewer_form"):
        game = st.text_input("Game Name")
        audience = st.text_input("Target Audience")
        style = st.text_input("Preferred Style")
        content_type = st.text_input("Type of Content")
        submitted = st.form_submit_button("Submit")
        if submitted:
            pb.BuildReviewerPrompt(
                callback=display_callback,
                ie=ie,
                game=game,
                audience=audience,
                style=style,
                content_type=content_type,
            )
