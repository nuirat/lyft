from car import Car
from engines.capulet import CapuletEngine
from batteries.spindler import SpindlerBattery

class Calliope(Car):
    def __init__(self, current_mileage, last_service_mileage, last_service_date):
        calliope_engine = CapuletEngine(current_mileage, last_service_mileage)
        calliope_battery = SpindlerBattery(last_service_date)

        super().__init__(calliope_engine, calliope_battery)

        self.engine = calliope_engine
        self.battery = calliope_battery

    def needs_service(self):
        return super().needs_service()