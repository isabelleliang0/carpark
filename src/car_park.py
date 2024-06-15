from sensor import Sensor
from display import Display
from pathlib import Path
from datetime import datetime
import json

class CarPark:
    pass

    def __init__(self,
                 location,
                 capacity,
                 log_file = Path("log.txt"),
                 config_file = Path("Config.json"),
                 plates = None,
                 sensors = None,
                 displays = None):
        self.location = location
        self.capacity = capacity
        self.plates = plates or []
        self.sensors = sensors or []
        self.displays = displays or []
        self.log_file = log_file if isinstance(log_file, Path) else Path(log_file)
        self.log_file.touch(exist_ok=True)
        self.config_file = Path(config_file)

    def write_config(self):
        with open(self.config_file, "w") as f:
            json.dump({"location": self.location,
                       "capacity": self.capacity,
                       "log_file": str(self.log_file)}, f)

    # ... inside the CarPark class
    @staticmethod
    def from_config(cls, config_file=Path("config.json")):
        config_file = config_file if isinstance(config_file, Path) else Path(config_file)
        with config_file.open() as f:
            config = json.load(f)
        return cls(config["location"], config["capacity"], log_file=config["log_file"])

    def __str__(self):
        return f'Car park at {self.location}, with {self.capacity} bays.'


    def register(self, component):
        if not isinstance(component, (Sensor, Display)):
            raise TypeError("Invalid component type.")

        if isinstance(component, Sensor):
            self.sensors.append(component)
        elif isinstance(component, Display):
            self.displays.append(component)

    def _log_car(self, action, plate):
        with self.log_file.open(mode = "a") as file:
            file.write(f'{plate} {action} on the {datetime.now().strftime("%d-%m %H:%M")}\n')

    def add_car(self, plate):
        self.plates.append(plate)
        self.update_displays()
        self._log_car("entered", plate)

    def remove_car(self, plate):
        self.plates.remove(plate)
        self.update_displays()
        self._log_car("exited", plate)


    def update_displays(self):
        for display in self.displays:
            display.update({"Bays": self.available_bays,
                            "Temperature": 25 })
            print(f'Updating: {display}')

    @property
    def available_bays(self):
        #car_park.available_bays b/c its an attribute
        return max(0, self.capacity - len(self.plates))

    # in CarPark class
    def _log_car_activity(self, plate, action):
        with self.log_file.open("a") as f:
            f.write(f"{plate} {action} at {datetime.now()}\n")
