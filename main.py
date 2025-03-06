from google_gemini_api import GoogleGenerativeAI
from prompt_component import PromptComponent
import os
from dotenv import load_dotenv

load_dotenv()


class AIResponseGenerator:
    def __init__(self, api_key, prompt_template):
        self.gemini = GoogleGenerativeAI(api_key=api_key)
        self.prompt_component = PromptComponent(prompt_template)
    
    def generate_response(self, **kwargs):
        """Fills in the prompt template and gets a response from Gemini AI."""
        prompt = self.prompt_component.build_prompt(**kwargs)
        return self.gemini.generate_text(prompt)

# Example Usage
api_key = os.getenv("GEMINI_API_KEY")
prompt_template = "Explain {topic} in detail."
ai_response_generator = AIResponseGenerator(api_key, prompt_template)
response = ai_response_generator.generate_response(topic="AI")
print(response)
