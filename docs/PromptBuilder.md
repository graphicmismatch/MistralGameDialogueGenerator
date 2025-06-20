# PromptBuilder.py

This script is responsible for generating structured prompt templates to be sent to a language model via the InferenceEngine. It provides flexible and context-aware dialogue generation tools for casual game development, game reviews, and professional game writing workflows.

## Methods

- **PromptBuilder.\_\_init\_\_**(
  self,
  character\_file: str
  )

  - Constructor for the PromptBuilder class. Loads character data from a specified JSON file.
  - **Parameters:**

    - **self:** the class instance.
    - **character\_file:** path to a JSON file containing character metadata (e.g. name, personality, role, backstory).

- **PromptBuilder.BuildCasualPrompt**(
  callback,
  ie: InferenceEngine,
  character: str,
  theme: str,
  mood: str,
  situation: str
  )

  - Builds and sends a prompt for generating casual in-game dialogue using a specified theme, mood, and situation.
  - **Parameters:**

    - **callback:** the function to call when the model returns a response.
    - **ie:** an instance of InferenceEngine.
    - **character:** name of the character; if empty, a random character is used.
    - **theme:** the design theme; if empty, it is randomized.
    - **mood:** emotional tone; randomized if left blank.
    - **situation:** the game situation; randomized if unspecified.

- **PromptBuilder.load\_character**(
  self,
  path: str
  ) → dict

  - Loads and parses the character JSON data from the given file path.
  - **Parameters:**

    - **self:** the class instance.
    - **path:** file path to the character JSON file.
  - **Returns:**

    - A dictionary with character details (name, personality, role, backstory).

- **PromptBuilder.BuildReviewerPrompt**(
  callback,
  ie: InferenceEngine,
  game: str,
  audience: str,
  style: str,
  content\_type: str
  )

  - Builds and sends a prompt to generate creative content for a game reviewer or influencer.
  - **Parameters:**

    - **callback:** the function to call with the generated response.
    - **ie:** an instance of InferenceEngine.
    - **game:** the game title; if empty, it will be randomized.
    - **audience:** the target audience; if empty, randomized.
    - **style:** content style (e.g. humorous, analytical); defaults to random if blank.
    - **content\_type:** the content format (e.g. video script, tweet); randomized if not specified.

- **PromptBuilder.build\_prompt**(
  self,
  situation: str
  ) → str

  - Constructs a prompt string using character metadata and the given situation.
  - **Parameters:**

    - **self:** the class instance.
    - **situation:** the situation/context to base the dialogue on.
  - **Returns:**

    - A formatted string prompt suitable for in-character dialogue generation.

- **PromptBuilder.GetProfessionalGameDeveloper**(
  callback,
  ie: InferenceEngine,
  length: str,
  theme: str,
  setting: str,
  context: str,
  characters: str,
  mood: str
  )

  - Builds and sends a professional-grade game dialogue prompt, using parameters suitable for narrative or design purposes.
  - Includes detailed instructions to avoid clichés and produce natural conversation.
  - Automatically randomizes any unspecified parameter and provides brief explanations for random values.
  - Uses Few-Shot Learning examples to guide the model's output format and tone.
  - **Parameters:**

    - **callback:** the function to be called with the generated response.
    - **ie:** an instance of InferenceEngine.
    - **length:** maximum dialogue length; randomized if blank.
    - **theme:** theme of the game; randomized if not provided.
    - **setting:** setting of the dialogue; randomized if blank.
    - **context:** the narrative context; defaults to random if unspecified.
    - **characters:** list or number of characters; randomized if not given.
    - **mood:** the mood/tone of the dialogue; randomized if left blank.
