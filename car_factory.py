from car import Car

from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine

from Battery.nubbin_battery import NubbinBattery
from Battery.splinder_battery import SplinderBattery


class CarFactory(Car):

    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage):
        engine = CapuletEngine(last_service_date, current_mileage, last_service_mileage)
        battery = SplinderBattery(last_service_date)
        car = Car(engine, battery)
        return

    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage):
        engine = WilloughbyEngine(last_service_date, current_mileage, last_service_mileage)
        battery = SplinderBattery(last_service_date)
        car = Car(engine, battery)
        return car

    def create_palindrome(current_date, last_service_date, warning_light_on):

        engine = SternmanEngine(last_service_date, )
        battery = SplinderBattery(last_service_date)
        return Car

    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage):
        engine = WilloughbyEngine(last_service_date, current_mileage, last_service_mileage)
        battery = NubbinBattery(last_service_date)
        car = Car(engine, battery)
        return car

    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage):
        engine = CapuletEngine(last_service_date, current_mileage, last_service_mileage)
        battery = NubbinBattery(last_service_date)
        car = Car(engine, battery)
        return car
        