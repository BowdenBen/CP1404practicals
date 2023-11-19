"""
Unreliable Car Class
child of parent class (Car)
"""
from car import Car


class UnreliableCar(Car):
    """ Car class with a reliability object """

    def __init__(self, name, fuel, reliability: float):
        """ Initialise Car object, pulling from Car class parent, and adding reliability"""
        super().__init__(name, fuel)
        self.reliability = reliability
