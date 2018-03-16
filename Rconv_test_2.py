import unittest
from Rconv import RomanNumer


class RomanNumerTest(unittest.TestCase):

    def setUp(self):
        print('setUp')
        self.value = RomanNumer()
        
    def tearDown(self):
        print('tearDown')
        self.value = None;
    
    def test_parsing_millenia(self):
        self.assertEqual(1000, self.value.convert_to_decimal('M'))
    
    def test_parsing_century(self):
        self.assertEqual(100, self.value.convert_to_decimal('C'))
    
    def test_parsing_half_century(self):
        self.assertEqual(50, self.value.convert_to_decimal('L'))
    
    def test_parsing_decade(self):
        self.assertEqual(10, self.value.convert_to_decimal('X'))
    
    def test_parsing_half_decade(self):
        self.assertEqual(5, self.value.convert_to_decimal('V'))
    
    def test_parsing_one(self):
        self.assertEqual(1, self.value.convert_to_decimal('I'))
    
    def test_empty_roman_numeral(self):
        self.assertTrue(self.value.convert_to_decimal('') == 0)
        self.assertFalse(self.value.convert_to_decimal('') > 0)
    
    def test_no_roman_numeral(self):
        self.assertRaises(TypeError, self.value.convert_to_decimal, None)

if __name__=='__main__':
    unittest.main()
