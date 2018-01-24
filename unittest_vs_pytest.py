'''
Unittest comes with python default package
And pytest you need to install separately (pip install -U pytest)
'''

#Using Unittest

import unittest

def upper_reverse(text):
    return ''.join(reversed(text.upper()))
	
class TestUpperReversed(unittest.TestCase):
    def test_upper_reversed(self):
	    self.assertEqual(upper_reverse('hello'), 'OLLEH')

if __name__=='__main__':
    unittest.main()
		
'''		
#Using pytest

def upper_reverse(text):
    return ''.join(reversed(text.upper()))

def test_upper_reverse():
	assert upper_reverse('hello') == 'OLLEH'	
	
'''
