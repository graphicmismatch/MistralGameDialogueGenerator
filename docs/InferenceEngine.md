# InferenceEngine.py

This module acts as the interface between your application and the **Mistral** language model. It abstracts away the complexity of asynchronous programming and provides an easy-to-use API for sending prompts (including few-shot examples) to Mistral.

It includes support for:

- System and user prompts
- Few-shot learning with structured examples
- Temperature control (model creativity)
- Synchronous execution via an async event loop wrapper

## Utility Functions

- **run\_async\_task**(coro)
  - A helper function that safely executes asynchronous coroutines within environments (like Streamlit) that don't natively support `async/await`.
  - **Parameters:**
    - **coro:** `coroutine` — The asynchronous task to be executed.
  - **Returns:**
    - The result of the coroutine, executed synchronously.

## Data Classes

- **FSLData**
  - A lightweight container to store Few-Shot Learning examples.
  - **Attributes:**
    - **prompt:** `str` — The example input prompt.
    - **response:** `str` — The expected model output for the prompt.

## Class: InferenceEngine

- **InferenceEngine.\_\_init\_\_**(
    self,
    modelname: str = "mistral-small-2503",
    temp: float = 0.2
)

  - Initializes the inference engine with a specific model and temperature setting. Loads the Mistral API key from a .env file.
  - **Parameters:**
    - **modelname:** `str` — Name of the model to use (default is `"mistral-small-2503"`).
    - **temp:** `float` — Default temperature (creativity) setting (default is `0.2`).

- **InferenceEngine.GivePrompt**(
    self,
    callback,
    userprompt: str,
    systemprompt: str = None,
    learning: List\[FSLData] = None,
    temp: float = None
)
  - Formats and submits a prompt to the Mistral model. Supports system prompts, few-shot learning examples, and optional temperature override.
  - **Parameters:**
    - **callback:** `function` — Function to execute when the model returns a result.
    - **userprompt:** `str` — The main prompt/question to ask the model.
    - **systemprompt:** `str` — A system-level instruction (optional).
    - **learning:** `List[FSLData]` — Optional few-shot learning examples.
    - **temp:** `float` — Optional override for the model temperature (default uses `self.temp`).
  - **Behavior:**
    - If learning examples are included, the system prompt is extended with formatting constraints.
    - Messages are formatted for Mistral’s `chat.complete_async` method.
    - Execution is handled synchronously via `run_async_task`.

- **InferenceEngine.PromptWorker**(
    self,
    callback,
    messagedict,
    temp: float
)

  - Handles the actual API call to Mistral. This is an asynchronous method wrapped by `run_async_task` in normal use.

  - **Parameters:**
    - **callback:** `function` — Function to call with the model response.
    - **messagedict:** `List[dict]` — A list of messages including system, user, and assistant roles.
    - **temp:** `float` — Temperature (creativity) value for this request.

## Example Usage

```python
ie = InferenceEngine()
ie.GivePrompt(
    callback=print,
    userprompt="Write a short fantasy dialogue",
    systemprompt="You are a world-class game writer.",
    learning=[
        FSLData(prompt="Who are you?", response="I'm a wandering bard with no name."),
    ],
)
```
