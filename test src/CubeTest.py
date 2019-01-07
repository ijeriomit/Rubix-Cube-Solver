import unittest
from Cube import Cube
import Piece
from CubeFaces import CubeFaces



class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.cf = CubeFaces()
        self.cf.FillCubeMatrix()
        self.cube = Cube(self.cf.cubematrix)

    def test_getpiece(self):
        self.assertEqual(Piece.EDGE, self.cube.get_piece((1, 1, 1)).piecetype)

    def test_getpiecethatdoesntexist(self):
        self.assertEqual(None, self.cube.get_piece((2, 1, 1)))

    def test_setpiececolors(self):
        self.cube.set_piece_colors(self.cf.cubematrix)
        print(self.cube.get_piece((0, 1, 1)).piececolors)


if __name__ == '__main__':
    unittest.main()
