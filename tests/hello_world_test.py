import unittest

from example.hello_world import HelloWorld

class HelloWorldTest(unittest.TestCase):

    def test_hello_world(self):
        x = HelloWorld()
        x.say()
 
if __name__ == "__main__":
        unittest.main()
