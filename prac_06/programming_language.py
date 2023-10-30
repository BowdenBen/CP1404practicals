"""
time estimate: 3 hours
actual time:
"""

class ProgrammingLanguage:

    def __init__(self, name="", typing=False, reflection=False, year=0):
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        return self.typing == "Dynamic"
