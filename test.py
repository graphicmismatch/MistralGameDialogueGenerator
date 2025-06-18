# game_reviewer_test.py

from src.GameReviewerPromptBuilder import GameReviewerPromptBuilder

from src.InferenceEngine import InferenceEngine

from src.PromptBuilder import PromptBuilder

# --- Game Reviewer Prompt Building ---

def review_game():

    reviewer_builder = GameReviewerPromptBuilder("reviewer.json")

    game_summary = (

        "A pixel-art platformer where a frog battles capitalist robots to reclaim his swamp."

    )

    reviewer_prompt = reviewer_builder.build_prompt(game_summary)

    print("Game Reviewer Prompt:\n")

    print(reviewer_prompt)

    print("\n" + "-" * 80 + "\n")

# --- Jarvis Prompt Inference ---

def jarvis_response():

    inference_engine = InferenceEngine(temp=0.2)

    jarvis_builder = PromptBuilder("characters/jarvis.json")

    prompt = jarvis_builder.build_prompt(

        "The player just landed on Mars and asks if it's safe to remove their helmet."

    )

    def handle_response(response):

        print("Jarvis says:\n")

        print(response.choices[0].message.content)

    inference_engine.GivePrompt(

        callback=handle_response,

        userprompt=prompt

    )

# --- Main Execution ---

if __name__ == "__main__":

    review_game()

    jarvis_response()