import unittest
import classify


class SimpleTest(unittest.TestCase):

    def test_boundaries_type(self):
        boundaries = classify.getBoundaries()
        self.assertTrue(all(isinstance(elem, int) for elem in boundaries))

    def test_file_columns(self):
        file = open("marks.dat")
        results = classify.getData(file)
        self.assertLess(len(results[0]), 2, msg="Less than 2 columns in the first entry of the file.")

    def test_boundaries_length(self):
        self.assertIsNot(len(classify.boundaries), 0, "No boundaries are set.")

    

if __name__ == '__main__':
    unittest.main()
