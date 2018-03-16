import unittest
from Rconv import RomanNumer


class RomanNumerTest(unittest.TestCase):
    
    def test_parsing_millenia(self):
        value = RomanNumer("M")
        self.assertEqual(1000, value.convert_to_decimal())
    def test_parsing_century(self):
        value = RomanNumer("C")
        self.assertEqual(100, value.convert_to_decimal())
    def test_parsing_half_century(self):
        value = RomanNumer("L")
        self.assertEqual(50, value.convert_to_decimal())
    def test_parsing_decade(self):
        value = RomanNumer("X")
        self.assertEqual(10, value.convert_to_decimal())
    def test_parsing_half_decade(self):
        value = RomanNumer("V")
        self.assertEqual(5, value.convert_to_decimal())
    def test_parsing_one(self):
        value = RomanNumer("I")
        self.assertEqual(1, value.convert_to_decimal())
    def test_empty_roman_numeral(self):
        value = RomanNumer("")
        self.assertTrue(value.convert_to_decimal() == 0)
        self.assertFalse(value.convert_to_decimal() > 0)
    def test_no_roman_numeral(self):
        value = RomanNumer(None)
        self.assertRaises(TypeError, value.convert_to_decimal)
        
if __name__=='__main__':
    unittest.main()
