import unittest
from sensor import EntrySensor
from car_park import CarPark

class TestSensor(unittest.TestCase):
    def setUp(self):
        self.car_park = CarPark("123 Example Street", 100)
        self.entry_sensor = EntrySensor (1, self.car_park, True)

    def test_sensor_initialized_with_all_attributes(self):
        self.assertIsInstance(self.entry_sensor, EntrySensor)
        self.assertEqual(self.entry_sensor.id, 1)
        self.assertIsInstance(self.entry_sensor.car_park, CarPark)
        self.assertEqual(self.entry_sensor.is_active, True)

    def test_detect_vehcile(self):
        total_plates = len(self.car_park.plates)
        self.entry_sensor.detect_vehicle()
        total_plates_updated = len(self.car_park.plates)
        self.assertNotEqual(total_plates_updated, total_plates)
