

class Guitar:

    def __init__(self, name="", year=0, cost=0.0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"The {self.name}, first made in {self.year}, and costs ${self.cost:.2f}"

    def get_age(self):
        return 2023 - self.year

    def is_vintage(self):
        if self.get_age() >= 50:
            return "Vintage"
        else:
            return "not Vintage"




