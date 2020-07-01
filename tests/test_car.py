#if '__file__' in globals():
#    import os, sys
#    sys.path.append(os.path.join(os.path.dirname(__file__), '..'))


import unittest
#import Vehicle, Car
from qitqito.vehicle import Car


class CarTest(unittest.TestCase):
    def test_run(self):
        car = Car(10)
        self.assertEqual(car.velocity, 10)
