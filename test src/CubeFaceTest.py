import unittest
from CubeFace import CubeFace
from ImageIO import ImageIO


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.imageIO = ImageIO()
        self.cubeFace = CubeFace(0)

    def test_saveColorCellsFace_1(self):
        self.cubeFace.saveColorCells(self.imageIO.loadImage("1", ".jpg"))
        for i in range(0, 3):
            for j in range(0, 3):
                self.assertEqual(*self.cubeFace.colorcells[i][j], "RED")

    def test_saveColorCellsFace_2(self):
        self.cubeFace.saveColorCells(self.imageIO.loadImage(str(2), ".jpg"))
        self.assertEqual([[['BLUE'], ['YELLOW'], ['RED']], [['ORANGE'], ['WHITE'], ['YELLOW']], [['GREEN'], ['RED'], ['BLUE']]], self.cubeFace.colorcells)

    def test_saveColorCellsFace_3(self):
        self.cubeFace.saveColorCells(self.imageIO.loadImage(str(3), ".jpg"))
        self.assertEqual([[['BLUE'], ['WHITE'], ['YELLOW']], [['GREEN'], ['RED'], ['BLUE']], [['ORANGE'], ['RED'], ['BLUE']]], self.cubeFace.colorcells)

    def test_saveColorCellsFace_4(self):
        self.cubeFace.saveColorCells(self.imageIO.loadImage("4", ".jpg"))
        for i in range(0, 3):
            for j in range(0, 3):
                self.assertEqual(*self.cubeFace.colorcells[i][j], "BLUE")

    def test_saveColorCellsFace_5(self):
        self.cubeFace.saveColorCells(self.imageIO.loadImage("5", ".jpg"))
        for i in range(0, 3):
            for j in range(0, 3):
                self.assertEqual(*self.cubeFace.colorcells[i][j], "ORANGE")

    def test_saveColorCellsFace_6(self):
        self.cubeFace.saveColorCells(self.imageIO.loadImage("6", ".jpg"))
        for i in range(0, 3):
            for j in range(0, 3):
                self.assertEqual(*self.cubeFace.colorcells[i][j], "YELLOW")


if __name__ == '__main__':
    unittest.main()
