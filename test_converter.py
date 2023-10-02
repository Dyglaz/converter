import unittest
from converter import Converter


class TestConverter(unittest.TestCase):
    def test_convert_length(self):
        self.assertAlmostEqual(Converter.convert_length(10, 'in', 'm'), 0.254, 3)
        self.assertAlmostEqual(Converter.convert_length(2, 'ft', 'm'), 0.6096, 3)
        self.assertAlmostEqual(Converter.convert_length(3, 'yd', 'm'), 2.7432, 3)
        self.assertAlmostEqual(Converter.convert_length(5, 'mi', 'm'), 8046.72, 3)
        self.assertAlmostEqual(Converter.convert_length(20, 'mi', 'yd'), 35200, 3)

    def test_convert_weight(self):
        self.assertAlmostEqual(Converter.convert_weight(20, 'oz', 'kg'), 0.567, 3)
        self.assertAlmostEqual(Converter.convert_weight(8, 'lb', 'kg'), 3.629, 3)
        self.assertAlmostEqual(Converter.convert_weight(2, 'лот', 'g'), 25.594, 3)
        self.assertAlmostEqual(Converter.convert_weight(5, 'золотник', 'g'), 21.33, 3)
        self.assertAlmostEqual(Converter.convert_weight(10, 'kg', 'lb'), 22.046, 3)