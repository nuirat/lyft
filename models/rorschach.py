from car import Car
from engines.willoughby import WilloughbyEngine
from batteries.nubbin import NubbinBattery

class Rorschach(Car):
    def __init__(self, current_mileage, last_service_mileage, last_service_date):
        rorschach_engine = WilloughbyEngine(current_mileage, last_service_mileage)
        rorschach_battery = NubbinBattery(last_service_date)

        super().__init__(rorschach_engine, rorschach_battery)

        self.engine = rorschach_engine
        self.battery = rorschach_battery

    def needs_service(self):
        return super().needs_service()