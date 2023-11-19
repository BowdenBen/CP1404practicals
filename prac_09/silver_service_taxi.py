"""
Silver Service Taxi Class
child of taxi class
"""
from taxi import Taxi


class SilverServiceTaxi(Taxi):
    """ A child of the taxi class, therefore inherits from taxi and car classes """

    def __init__(self, name, fuel, fanciness: float):
        """ passing in Car class objects, adding fanciness object """
        super().__init__(name, fuel)
        self.price_per_km = Taxi.price_per_km * fanciness  # fanciness is a scaler of all taxi's price per km
