from src. GameReviewerPromptBuilder import  GameReviewerPromptBuilder
builder = GameReviewerPromptBuilder("reviewer.json")
game_summary = "A pixel-art platformer where a frog battles capitalist robots to reclaim his swamp."
print(builder.build_prompt(game_summary))
