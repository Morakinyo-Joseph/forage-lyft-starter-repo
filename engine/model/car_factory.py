from car import Car


class CarFactory(Car):

    def create_calliope(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int):
        car = Car('Calliope')
        car.set_current_date(current_date)
        car.set_last_service_date(last_service_date)
        car.set_current_mileage(current_mileage)
        car.set_last_service_mileage(last_service_mileage)
        return car

    def create_glissade(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int):
        car = Car('Glissade')
        car.set_current_date(current_date)
        car.set_last_service_date(last_service_date)
        car.set_current_mileage(current_mileage)
        car.set_last_service_mileage(last_service_mileage)
        return car

    def create_palindrome(current_date: date, last_service_date: date, warning_light_on: bool):
        car = Car('Palindrome')
        car.set_current_date(current_date)
        car.set_last_service_date(last_service_date)
        car.set_warning_light_on(warning_light_on)
        return car

    def create_rorschach(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int):
        car = Car('Rorschach')
        car.set_current_date(current_date)
        car.set_last_service_date(last_service_date)
        car.set_current_mileage(current_mileage)
        car.set_last_service_mileage(last_service_mileage)
        return car

    def create_thovex(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int):
        car = Car('Thovex')
        car.set_current_date(current_date)
        car.set_last_service_date(last_service_date)
        car.set_current_mileage(current_mileage)
        car.set_last_service_mileage(last_service_mileage)
        return car
        
