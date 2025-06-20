import json
from pathlib import Path
from utils.InferenceEngine import *


class PromptBuilder:
    def __init__(self, character_file: str):
        self.character_data = self.load_character(character_file)

    def BuildCasualPrompt(
        callback,
        ie: InferenceEngine,
        character: str,
        theme: str,
        mood: str,
        situation: str,
    ):
        if character.strip() == "":
            character = "<random>"
        if theme.strip() == "":
            theme = "<random>"
        if mood.strip() == "":
            mood = "<random>"
        if situation.strip() == "":
            situation = "<random>"
        systemprompt = "Generate immersive and fun character dialogue for a casual game developer based on the input."
        prompt = f"""
        Generate a dialogue based on the following casual game design input:

        - Character: {character}
        - Theme: {theme}
        - Mood: {mood}
        - Situation: {situation}

        Respond as if it's a game scene script between characters. Keep the tone light and imaginative.
        """

        ie.GivePrompt(
            callback=callback,
            userprompt=prompt,
            systemprompt=systemprompt,
        )

    def load_character(self, path: str) -> dict:
        character_path = Path(path)
        if not character_path.exists():
            raise FileNotFoundError(f"Character file {path} not found.")
        with open(character_path, "r", encoding="utf-8") as file:
            return json.load(file)

    def BuildReviewerPrompt(
        callback,
        ie: InferenceEngine,
        game: str,
        audience: str,
        style: str,
        content_type: str,
    ):
        if game.strip() == "":
            game = "<random>"
        if audience.strip() == "":
            audience = "<random>"
        if style.strip() == "":
            style = "<random>"
        if content_type.strip() == "":
            content_type = "<random>"
        systemprompt = "You are helping a game reviewer/influencer create content that is fresh, engaging, and tailored for their audience."
        prompt = """
        Generate creative content for a game reviewer or influencer with the following details:

        - Game: {game}
        - Target Audience: {audience}
        - Style: {style}
        - Content Type: {content_type}

        Ensure the content is catchy, engaging, and suitable for social media or video commentary.
        Keep it concise and audience-appropriate.
        """

        ie.GivePrompt(
            callback=callback,
            userprompt=prompt,
            systemprompt=systemprompt,
        )

    def build_prompt(self, situation: str) -> str:
        name = self.character_data.get("name", "Unknown")
        personality = self.character_data.get("personality", "")
        role = self.character_data.get("role", "")
        backstory = self.character_data.get("backstory", "")

        return (
            f"You are {name}, a {personality} {role}. "
            f"Your backstory: {backstory}.\n"
            f"Situation: {situation}\n"
            f"Respond in character."
        )

    def GetProfessionalGameDeveloper(
        callback,
        ie: InferenceEngine,
        length: str,
        theme: str,
        setting: str,
        context: str,
        characters: str,
        mood: str,
    ):
        systemprompt = """
        The user is a professional game developer. 
        Your job is to help the user write a natural sounding dialogue a few parameters.
        In order to make the dialogue sound natural:
            - avoid cliches
            - avoid going in a fixed conversation order. conversations can be messy, especially between many people.
            - avoid starting the each line with a pronoun.
            - do not shy away from adding conflict if it makes sense in context. 
        If any of the data is given as "<random>", that indicates that the user has not provided any data.
        When the user has not provided any data, the parameter can be randomized.
        ONLY IF a parameter is randomized, before the dialogue is generated, give a one-line explanation of the set value(s) (if character is randomized, you should give one line about each character, if the theme is randomized, you should explain the set theme, etc)
        Avoid controversial topics unless the user specifically requests for them.
        
        Remove any unnecessary indentation.
        """

        if length == "":
            length = "<random>"
        if theme == "":
            theme = "<random>"
        if setting == "":
            setting = "<random>"
        if context == "":
            context = "<random>"
        if characters == "":
            characters = "<random>"
        if mood == "":
            mood = "<random>"

        prompt = f"""
        Generate a dialogue with the following specifications:
        
        1) Maximum dialogue length: {length}
        2) Theme: {theme}
        3) Setting: {setting}
        4) Context: {context}
        5) Characters: {characters}
        6) Mood: {mood}
        """
        example1 = FSLData(
            """
        Generate a dialogue with the following specifications:
        
        1) Maximum dialogue length: 6
        2) Theme: sci-fi
        3) Setting: Jupiter
        4) Context: 2 humans meet on jupiter for the first time in the far future
        5) Characters: 2
        6) Mood: funny
        """,
            """
        Blorg> Hey!\n\n**Blingus>** Whats Up?\n\n**Blorg>** Nothing much, trying not to freeze here... Jupiter is much colder than Earth\n\n**Blingus>** Seriously, it is unbearable. I'm Blingus, what is your name?\n\n**Blorg>** I'm Blorg, nice to meet you!\n\n**Blingus>** Nice to meet you too!
        """,
        )

        example2 = FSLData(
            """
        Generate a dialogue with the following specifications:
        
        1) Maximum dialogue length: 6
        2) Theme: fantasy
        3) Setting: a forest
        4) Context: zeke and jake are trying to find the last remaining elf.
        5) Characters: zeke, jake
        6) Mood: serious
        """,
            """
        Zeke> Jake! Did you find anything?\n\n**Jake>** No, not a single trace of her.\n\n**Zeke>** HOW HARD IS IT TO FIND ONE OLD ELF?\n\n- after 5 minutes -\n\n**Zeke>** Hey! I found something. Come here!\n\n**Jake>** Woah, its a burrow, do you think the elf would be in there?\n\n**Zeke>** She could be! Lets check it out
        """,
        )

        example3 = FSLData(
            """
        Generate a dialogue with the following specifications:
        
        1) Maximum dialogue length: 6
        2) Theme: fantasy
        3) Setting: a forest
        4) Context: a few humans are trying to find the last remaining elf.
        5) Characters: <random>
        6) Mood: serious
        """,
            """
        - **Characters:**\n\t1. **Zeke:** Cool guy tbh\n\t2. **Jake:** thinks zeke has a cool name\n\n___\n\n**Zeke>** Jake! Did you find anything?\n\n**Jake>** No, not a single trace of her.\n\n**Zeke>** HOW HARD IS IT TO FIND ONE OLD ELF?\n\n- after 5 minutes -\n\n**Zeke>** Hey! I found something. Come here!\n\n**Jake>** Woah, its a burrow, do you think the elf would be in there?\n\n**Zeke>** She could be! Lets check it out
        """,
        )

        example4 = FSLData(
            """
        Generate a dialogue with the following specifications:
        
        1) Maximum dialogue length: 6
        2) Theme: <random>
        3) Setting: a forest
        4) Context: a few humans are trying to find the last remaining elf.
        5) Characters: <random>
        6) Mood: serious
        """,
            """
        - **Theme:**\n\t- **Arcane Fantasy:** Arcane Fantasy blends magic with mysterious, fantastical worlds.\n\n___\n\n- **Characters:**\n\t1. **Zack:** aloof\n\t2. **Dyke:** curious\n\t3. **Bline:** very observant\n\n\n\n___\n\n\n\n**Bline>** Guys! Did you find anything?\n\n**Dyke>** No, not a single trace of her.\n\n**Zack>** HOW HARD IS IT TO FIND ONE OLD ELF?\n\n- after 25 minutes -\n\n**Bline>** Hey Guys! I found something. Come here!\n\n**Zack>** Woah, its a burrow, do you think the elf would be in there?\n\n**Dyke>** She could be! Lets check it out
        """,
        )

        example5 = FSLData(
            """
        Generate a dialogue with the following specifications:
        
        1) Maximum dialogue length: 6
        2) Theme: <random>
        3) Setting: a forest
        4) Context: a few humans are trying to find the last remaining elf.
        5) Characters: <random>
        6) Mood: serious
        """,
            """
        - **Theme:**\n\t- **Sci-fi:** Sci-fi explores futuristic concepts, advanced technology, and the impact of science on society.\n\n___\n\n- Characters:\n\t1. **Mac:** kinda pretentious\n\t2. **Loki:** patient\n\n\n\n___\n\n\n\n**Loki>** Mac! Did you find anything?\n\n**Mac>** No, not a single trace of her.\n\n**Mac>** HOW HARD IS IT TO FIND ONE OLD ELF?\n\n- after 7 minutes -\n\n**Mac>** Hey! I found something. Come here!\n\n**Loki>** Woah, its a laser pistol, do you think the elf dropped it?\n\n**Mac>** She could be! Lets check it out
        """,
        )
        examples = [example1, example2, example3, example4, example5]
        ie.GivePrompt(
            systemprompt=systemprompt,
            userprompt=prompt,
            learning=examples,
            callback=callback,
        )
