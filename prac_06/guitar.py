

class Guitar:
    """Create Guitar class"""
    def __init__(self, name="", year=0, cost=0.0):      # initialise class variables
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):      # return a string involving all variables
        return f"The {self.name}, first made in {self.year}, and costs ${self.cost:.2f}"

    def get_age(self):      # return an age
        return 2023 - self.year

    def is_vintage(self):       # return boolean if age is greater than 50
        return self.get_age() >= 50




