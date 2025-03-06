import unittest
from unittest.mock import patch, MagicMock
from google_gemini_api import GoogleGenerativeAI

class TestGoogleGenerativeAI(unittest.TestCase):
    
    @patch("requests.post")
    def test_generate_text_success(self, mock_post):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "candidates": [{
                "content": {"parts": [{"text": "AI is a branch of computer science that focuses on building smart machines."}]}
            }]
        }
        mock_post.return_value = mock_response
        
        api = GoogleGenerativeAI(api_key="fake_api_key")
        response = api.generate_text("What is AI?")
        
        self.assertEqual(response, "AI is a branch of computer science that focuses on building smart machines.")
    
    @patch("requests.post")
    def test_generate_text_error(self, mock_post):
        mock_response = MagicMock()
        mock_response.status_code = 400
        mock_response.text = "Invalid API Key"
        mock_post.return_value = mock_response
        
        api = GoogleGenerativeAI(api_key="invalid_key")
        response = api.generate_text("Explain AI")
        
        self.assertEqual(response, "Error: Invalid API Key")

if __name__ == "__main__":
    unittest.main()
