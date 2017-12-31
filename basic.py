class Hello(object):

  def get_message(self):

     return "Hello World"


  def anna_viesti(self):

     return "Hei Maailma!"


import unittest


class Test(unittest.TestCase):


    # Creates the Hello-object being tested. 
    # You could do this in the test-methods as well.
    
    def setUp(self):

        self.hello = Hello()


    # Tests the english method for the string "Hello World!".

    def test_english(self):

        output = self.hello.get_message()

        self.assertEqual(output,
                      "Hello World",
                      "get_message() does not output the correct value.")


    # Tests the finnish method for the string "Hei Maailma!".

    def test_finnish(self):

        output = self.hello.anna_viesti()

        self.assertEqual(output,
                         "Hei Maailma!",
                         "hae_viesti() does not output the correct value.")

if __name__ == "__main__":
    unittest.main()
