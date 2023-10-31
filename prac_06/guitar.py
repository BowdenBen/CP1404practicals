"""
Create Guitar class to process guitar list from inputs
"""


class Guitar:
    """Create Guitar class"""
    def __init__(self, name="", year=0, cost=0.0):
        """Set variables for object"""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return Variables as a string"""
        return f"The {self.name}, first made in {self.year}, and costs ${self.cost:.2f}"

    def __repr__(self):
        """Return list of variables as designated string"""
        return str(self)

    def get_age(self):
        """Return age, worked out from this year and date manufactured"""
        return 2023 - self.year

    def is_vintage(self):
        """Return if vintage or not using boolean"""
        if self.get_age() >= 50:
            return "Vintage"
        else:
            return "Not Vintage"




