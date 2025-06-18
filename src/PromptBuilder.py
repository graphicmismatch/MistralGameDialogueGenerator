import json
from pathlib import Path

class PromptBuilder:
    def __init__(self, character_file: str):
        self.character_data = self.load_character(character_file)

    def load_character(self, path: str) -> dict:
        character_path = Path(path)
        if not character_path.exists():
            raise FileNotFoundError(f"Character file {path} not found.")
        with open(character_path, "r", encoding="utf-8") as file:
            return json.load(file)

    def build_prompt(self, situation: str) -> str:
        name = self.character_data.get("name", "Unknown")
        personality = self.character_data.get("personality", "")
        role = self.character_data.get("role", "")
        backstory = self.character_data.get("backstory", "")

        return (
            f"You are {name}, a {personality} {role}. "
            f"Your backstory: {backstory}.\n\n"
            f"Situation: {situation}\n"
            f"Respond in character."
        )
