import unittest
from Cube import Cube
import Piece
from CubeFaces import CubeFaces
import ColorPicker as cp



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
        for piece in self.cube.pieces:
            self.assertNotIn(None, piece.colors)

    def test_setpieccolorswithedges(self):
        self.cube.set_piece_colors(self.cf.cubematrix)
        self.assertIn((cp.WHITE, "UP"), self.cube.edges[0].colors)
        self.assertIn((cp.GREEN, "RIGHT"), self.cube.edges[0].colors)
        self.assertIn((cp.ORANGE, "FRONT"), self.cube.edges[0].colors)

    def test_get_pieces_by_xpos(self):
        self.assertEqual(9, len(self.cube.get_pieces_by_xpos(1)))


if __name__ == '__main__':
    unittest.main()
