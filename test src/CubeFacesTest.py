import unittest
from CubeFaces import CubeFaces

class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.cubemat = CubeFaces(".jpg")

    def test_something(self):
        self.cubemat.FillCubeMatrix()

        for i in range(0, 6):
            print(self.cubemat.cubematrix[i])


if __name__ == '__main__':
    unittest.main()
