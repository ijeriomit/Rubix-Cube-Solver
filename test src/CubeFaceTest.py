import unittest
from CubeFace import CubeFace
from ImageIO import ImageIO

class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.imageIO = ImageIO()
        self.cubeFace = CubeFace(self.imageIO.loadImage(str(1), ".jpg"), 0)

    def test_initFace(self):
        self.cubeFace.initFace()
        for i in range(0, 3):
            for j in range(0, 3):
                self.assertEqual(*self.cubeFace.cells[i][j], "RED")

    def test_initializeMixedFace_1(self):
        self.cubeFace.setImage(self.imageIO.loadImage(str(2), ".jpg"))
        self.assertEqual([[['BLUE'], ['YELLOW'], ['RED']], [['ORANGE'], ['WHITE'], ['YELLOW']], [['GREEN'], ['RED'], ['BLUE']]], self.cubeFace.cells)

    def test_initializeMixedFace_2(self):
        self.cubeFace.setImage(self.imageIO.loadImage(str(3), ".jpg"))
        self.assertEqual([[['BLUE'], ['WHITE'], ['YELLOW']], [['GREEN'], ['RED'], ['BLUE']], [['ORANGE'], ['RED'], ['BLUE']]], self.cubeFace.cells)







if __name__ == '__main__':
    unittest.main()
