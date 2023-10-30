"""
time estimate: 3 hours
actual time: 2 hours 30 min
"""


from programming_language import ProgrammingLanguage


def main():
    """ create language objects with variables"""
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    print(python)

    programming_languages = [python, ruby, visual_basic]

    print("The Dynamically typed languages are:")
    dynamic_typing(programming_languages)


def dynamic_typing(programming_languages):
    """ created function to handle loop"""
    for programming_language in programming_languages:
        if programming_language.is_dynamic():
            print(programming_language.name)


if __name__ == "__main__":
    main()
