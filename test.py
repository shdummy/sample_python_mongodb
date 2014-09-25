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
        
    #@unittest.skip("Skip this test")
    def skip_this_test(self):
        self.skipTest("Shouldn't happen")

def main():
    unittest.main()

if __name__ == "__main__":
    main()
