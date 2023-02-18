from car import Car
from engines.capulet import CapuletEngine
from batteries.spindler import SpindlerBattery
from tires.octoprime import OctoprimeTire

class Calliope(Car):
    def __init__(self, current_mileage, last_service_mileage, last_service_date, tire_sensor_data):
        calliope_engine = CapuletEngine(current_mileage, last_service_mileage)
        calliope_battery = SpindlerBattery(last_service_date)
        calliope_tire = OctoprimeTire(tire_sensor_data)

        super().__init__(calliope_engine, calliope_battery, calliope_tire)

        self.engine = calliope_engine
        self.battery = calliope_battery
        self.tire = calliope_tire
    
    def needs_service(self):
        return super().needs_service()