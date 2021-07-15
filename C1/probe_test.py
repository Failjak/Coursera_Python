import json
import unittest
from unittest.mock import patch

from probe import Asteroid


class TestAsteroid(unittest.TestCase):
    def setUp(self) -> None:
        self.asteroid = Asteroid(2440012)

    def test_name(self):
        self.assertEqual(
            self.asteroid.name, '440012 (2002 LE27)'
        )

    def test_diameter(self):
        self.assertEqual(
            self.asteroid.diameter, 820
        )