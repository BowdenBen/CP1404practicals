"""
time estimate: 3 hours
actual time:
"""

class ProgrammingLanguage:

    def __init__(self, typing=False, reflection=False, year=0):
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        if self.typing:
            typing_type = "dynamic"
        else:
            typing_type = "static"
        return typing_type