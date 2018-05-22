import unittest
import classify as clify

class SimpleTest(unittest.TestCase):

    def test_boundaries_type(self,boundaries):
        self.assertTrue(all(isinstance(elem, int) for elem in boundaries))

    

if __name__ == '__main__':
    unittest.main()
