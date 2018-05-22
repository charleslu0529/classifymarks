import unittest
import classify

class SimpleTest(unittest.TestCase):

    def test_boundaries_type(self):
        boundaries=[0,49,59,69,74,100] #boundaries = classify.boundaries
        self.assertTrue(all(isinstance(elem, int) for elem in boundaries))

    def test_file_columns(self):
        test_file = open("marks.dat")
        results = []
        for lines in testFile:
            line = test_file.readline.split()
            results.append(line)
        self.assertLess(len(results[0]), 2, msg="Less than 2 columns in the first entry of the file.")

    def test_boundaries_length(self):
        self.assertIsNot(len(classify.boundaries), 0, "No boundaries are set.")

if __name__ == '__main__':
    unittest.main()
