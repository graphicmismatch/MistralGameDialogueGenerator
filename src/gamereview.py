import json
from pathlib import Path

class GameReviewerPromptBuilder:
    def __init__(self, reviewer_file: str):
        self.reviewer_data = self.load_reviewer_profile(reviewer_file)

    def load_reviewer_profile(self, path: str) -> dict:
        try:
            reviewer_path = Path(path)
            if not reviewer_path.exists():
                raise FileNotFoundError(f"Reviewer profile file '{path}' not found.")

            with open(reviewer_path, "r", encoding="utf-8") as file:
                return json.load(file)

        except FileNotFoundError as e:
            print(f"[ERROR] {e}")
            return {}
        except json.JSONDecodeError:
            print(f"[ERROR] Failed to decode JSON in file '{path}'. Please check the file format.")
            return {}

    def build_prompt(self, game_summary: str) -> str:
        name = self.reviewer_data.get("name", "Unknown Reviewer")
        review_style = self.reviewer_data.get("review_style", "neutral")
        specialty = self.reviewer_data.get("specialty", "general games")
        bio = self.reviewer_data.get("bio", "an experienced critic")

        prompt = (
            f"Your name is {name}. You are a {review_style} reviewer specializing in {specialty}, "
            f"known for being {bio}.\n\n"
            f"Write a detailed review of the following game in your signature style:\n"
            f"{game_summary}\n\n"
            f"Make sure your tone reflects your personality and focus on aspects relevant to your expertise."
        )
        return prompt
