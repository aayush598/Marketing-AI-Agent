import requests

class GoogleGenerativeAI:
    def __init__(self, api_key, model="gemini-1.5-pro", temperature=0.1):
        self.api_key = api_key
        self.model = model
        self.temperature = temperature

    def generate_text(self, prompt):
        url = f"https://generativelanguage.googleapis.com/v1beta/models/{self.model}:generateContent?key={self.api_key}"
        payload = {
            "contents": [{
                "parts": [{"text": prompt}]
            }],
            "generationConfig": {
                "temperature": self.temperature
            }
        }
        headers = {"Content-Type": "application/json"}
        response = requests.post(url, json=payload, headers=headers)
        
        if response.status_code == 200:
            return response.json().get("candidates", [{}])[0].get("content", {}).get("parts", [{}])[0].get("text", "No response")
        else:
            return f"Error: {response.text}"

class TextInput:
    def __init__(self):
        self.input_text = ""
    
    def set_input(self, text):
        self.input_text = text
    
    def get_input(self):
        return self.input_text

class TextOutput:
    def __init__(self):
        self.output_text = ""
    
    def set_output(self, text):
        self.output_text = text
    
    def get_output(self):
        return self.output_text

# Example usage
api = GoogleGenerativeAI(api_key="GEMINI_API_KEY")
text_input = TextInput()
text_output = TextOutput()

text_input.set_input("Explain how AI works")
response = api.generate_text(text_input.get_input())
text_output.set_output(response)

print(text_output.get_output())
