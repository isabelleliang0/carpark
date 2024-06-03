from sensor import Sensor
from display import Display

class CarPark:
    pass

    def __init__(self, location, capacity, plates = None, sensors = None, displays = None):
        self.location = location
        self.capacity = capacity
        self.plates = plates or []
        self.sensors = sensors or []
        self.displays = displays or []

    def __str__(self):
        return f'Car park at {self.location}, with {self.capacity} bays.'


    def register(self, component):
        if not isinstance(component, (Sensor, Display)):
            raise TypeError("Invalid component type.")

        if isinstance(component, Sensor):
            self.sensors.append(component)
        elif isinstance(component, Display):
            self.displays.append(component)


    def add_car(self, plate):
        self.plates.append(plate)
        self.update_displays()

    def remove_car(self, plate):
        self.plates.remove(plate)
        self.update_displays()

    def update_displays(self):
        for display in self.displays:
            display.update({"Bays": self.available_bays,
                            "Temperature": 25 })
            print(f'Updating: {display}')

    @property
    def available_bays(self):
        #car_park.available_bays b/c its an attribute
        if len(self.plates) > self.capacity:
            return 0
        elif:
            return self.capacity - len(self.plates)

