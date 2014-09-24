import unittest
from mongo import Mongo
        
class OtherTests(unittest.TestCase):
    
    def test_passing(self):
        p = True
        self.failIf(p != True)
        
    def test_passing_too(self):
        p = True
        self.failIf(p != True)
        
    def test_passing_three(self):
        p = True
        self.failIf(p != True)


def main():
    unittest.main()

if __name__ == "__main__":
    main()
