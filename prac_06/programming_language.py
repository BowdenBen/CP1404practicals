"""
time estimate: 3 hours
actual time: 2 hours 30 min
"""

class ProgrammingLanguage:

    def __init__(self, name="", typing=False, reflection=False, year=0):
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        return f"{self.name}, {self.typing} typing, reflection = {self.reflection}, First appeared in {self.year}"

    def is_dynamic(self):
        return self.typing == "Dynamic"
