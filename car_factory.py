from car import Car

from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine

from battery.nubbin_battery import NubbinBattery
from battery.splinder_battery import SplinderBattery

from tires.carrigan_tire import CarriganTire
from tires.octoprime_tire import OctoprimeTire


class CarFactory:
    @staticmethod
    def create_calliope(last_service_date, current_mileage, last_service_mileage, tire_wear):
        engine = CapuletEngine(last_service_date, current_mileage, last_service_mileage)
        battery = SplinderBattery(last_service_date)
        tire = CarriganTire(tire_wear)
        car = Car(engine, battery, tire)
        return car

    @staticmethod
    def create_glissade(last_service_date, current_mileage, last_service_mileage, tire_wear):
        engine = WilloughbyEngine(last_service_date, current_mileage, last_service_mileage)
        battery = SplinderBattery(last_service_date)
        tire = OctoprimeTire(tire_wear)
        car = Car(engine, battery, tire)
        return car

    @staticmethod
    def create_palindrome(last_service_date, warning_light_on, tire_wear):
        engine = SternmanEngine(warning_light_on)
        battery = SplinderBattery(last_service_date)
        tire = CarriganTire(tire_wear)
        car = Car(engine, battery, tire)
        return car

    @staticmethod
    def create_rorschach(last_service_date, current_mileage, last_service_mileage, tire_wear):
        engine = WilloughbyEngine(last_service_date, current_mileage, last_service_mileage)
        battery = NubbinBattery(last_service_date)
        tire = OctoprimeTire(tire_wear)
        car = Car(engine, battery, tire)
        return car

    @staticmethod
    def create_thovex(last_service_date, current_mileage, last_service_mileage, tire_wear):
        engine = CapuletEngine(last_service_date, current_mileage, last_service_mileage)
        battery = NubbinBattery(last_service_date)
        tire = CarriganTire(tire_wear)
        car = Car(engine, battery, tire)
        return car
        
