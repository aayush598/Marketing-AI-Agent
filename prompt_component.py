class PromptComponent:
    def __init__(self, template: str):
        self.template = template
        self.status = ""

    def build_prompt(self, **kwargs) -> str:
        """Replaces placeholders in the template with provided keyword arguments."""
        prompt = self.template.format(**kwargs)
        self.status = prompt
        return prompt

    def update_template(self, new_template: str):
        """Updates the template with a new string."""
        self.template = new_template

    def update_frontend_node(self, new_template: str, values: dict):
        """Updates the template and fills in the values dynamically."""
        self.update_template(new_template)
        return self.build_prompt(**values)

# Example Usage
# prompt_component = PromptComponent("Hello, {name}!")
# print(prompt_component.build_prompt(name="Aayush"))
