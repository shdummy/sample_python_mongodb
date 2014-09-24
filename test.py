import unittest
from mongo import Mongo


class SomeTests(unittest.TestCase):
    
    def some_test(self):
        return True
        
    def failing_test(self):
        p = True
        self.failIf(p == True)

    def test(self):
        mongo = Mongo()
        mongo.populate()
        things = mongo.count()
        self.failIf(things != 5)
        
class OtherTests(unittest.TestCase):
    
    def test_passing(self):
        p = True
        self.failIf(p != 2)
        
    def test_passing_too(self):
        p = True
        self.failIf(p != 2)
        
    def test_passing_three(self):
        p = True
        self.failIf(p != 2)


def main():
    unittest.main()

if __name__ == "__main__":
    main()
