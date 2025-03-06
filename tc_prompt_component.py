import unittest
from prompt_component import PromptComponent

class TestPromptComponent(unittest.TestCase):
    
    def test_build_prompt(self):
        prompt_component = PromptComponent("Hello, {name}!")
        result = prompt_component.build_prompt(name="Aayush")
        self.assertEqual(result, "Hello, Aayush!")

    def test_update_template(self):
        prompt_component = PromptComponent("Hello, {name}!")
        prompt_component.update_template("Welcome, {user}!")
        result = prompt_component.build_prompt(user="Aayush")
        self.assertEqual(result, "Welcome, Aayush!")

    def test_update_frontend_node(self):
        prompt_component = PromptComponent("Hello, {name}!")
        result = prompt_component.update_frontend_node("Hi, {name}!", {"name": "Aayush"})
        self.assertEqual(result, "Hi, Aayush!")

if __name__ == "__main__":
    unittest.main()
