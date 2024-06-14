import unittest
from display import Display
from car_park import CarPark

class TestDisplay(unittest.TestCase):
    def setUp(self):
        self.display = Display(1, CarPark("123 Example Street", 100), "Welcome to the car park", True )
        self.carpark = CarPark("123 Example Street", 100)
# ... inside the TestDisplay class
    def test_display_initialized_with_all_attributes(self):
        self.assertIsInstance(self.display, Display)
        self.assertEqual(self.display.id, 1)
        self.assertEqual(self.display.message, "Welcome to the car park")
        self.assertEqual(self.display.is_on, True)
        self.assertIsInstance(self.display.car_park, CarPark)

    def test_update(self):
        self.display.update({"message": "Welcome to the car park"})
        self.assertEqual(self.display.message, "Welcome to the car park")