
from abc import ABC, abstractmethod
import random

class Sensor(ABC):
    pass

    def __init__(self, id, car_park, is_active = False):
        self.id = id
        self.is_active = is_active
        self.car_park = car_park

    def _scan_plate(self):
        return "FAKE-" + format(random.randint(0, 999), '03d')

    @abstractmethod
    def update_car_park(self, plate):
        pass
    #what update_car_park does depends on implementation of the subclass = polymorphism
    #using same pattern to implement different forms (subclass polymorphism - subclass determines form)
    def detect_vehicle(self):
        plate = self._scan_plate()
        self.update_car_park(plate)

    def __str__(self):
        return f'Sensor {self.id} is {self.is_active}.'


class EntrySensor(Sensor):
    def update_car_park(self, plate):
        self.car_park.add_car(plate)
        print(f"Incoming 🚘 vehicle detected. Plate: {plate}")

class ExitSensor(Sensor):
    #just to demonstrate scan on exit since its not a real scanner
    def _scan_plate(self):
        return random.choice(self.car_park.plates)

    def update_car_park(self, plate):
        self.car_park.remove_car(plate)
        print(f"Outgoing 🚗 vehicle detected. Plate: {plate}")


