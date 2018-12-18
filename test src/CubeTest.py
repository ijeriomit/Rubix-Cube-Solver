import unittest
from Cube import Cube

class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.cube = Cube(".jpg")

    def test_something(self):
        self.cube.FillCube()
        print(self.cube.cubematrix[1])

if __name__ == '__main__':
    unittest.main()
