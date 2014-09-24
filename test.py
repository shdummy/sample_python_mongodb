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

def main():
    unittest.main()

if __name__ == "__main__":
    main()
