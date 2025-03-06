# Google Generative AI API Integration

## Overview

This project provides a Python implementation to interact with Google Generative AI without using the `langflow` library. It includes:

- **GoogleGenerativeAI**: A class to generate text using Google's Generative AI API.
- **TextInput**: A class for handling user input.
- **TextOutput**: A class for storing and retrieving generated text.
- **Unit Tests**: A test suite using `unittest` to verify API interactions.

## Installation

### Prerequisites

- Python 3.9+
- Install dependencies:
  ```sh
  pip install -r requirements.txt
  ```

## Usage

### Initialize and Generate Text

```python
from google_gemini_api import GoogleGenerativeAI, TextInput, TextOutput

api = GoogleGenerativeAI(api_key="YOUR_GOOGLE_API_KEY")
text_input = TextInput()
text_output = TextOutput()

text_input.set_input("Explain how AI works")
response = api.generate_text(text_input.get_input())
text_output.set_output(response)

print(text_output.get_output())
```

### Running Tests

Run unit tests using:

```sh
python -m unittest test_google_gemini.py
```

## API Reference

- **API Endpoint:** `https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={api_key}`
- **Required Parameters:**
  - `api_key`: Your Google API key
  - `model`: AI model to use (default: `gemini-1.5-pro`)
- **Request Format:**
  ```json
  {
    "contents": [
      {
        "parts": [{ "text": "Your prompt here" }]
      }
    ],
    "generationConfig": {
      "temperature": 0.1
    }
  }
  ```

## License

This project is licensed under the MIT License.
