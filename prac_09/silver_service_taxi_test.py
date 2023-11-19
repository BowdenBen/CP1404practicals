"""
testing Silver Service Taxi Class.
"""


from silver_service_taxi import SilverServiceTaxi

silver_service_taxi = SilverServiceTaxi("Black & White", 100, fanciness=1.5)
print(silver_service_taxi)
silver_service_taxi.start_fare()
