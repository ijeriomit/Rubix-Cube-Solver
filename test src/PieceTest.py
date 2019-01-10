import unittest
import Piece
import ColorPicker as cp


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.piece = Piece.Piece(Piece.Piece.CENTER, (0, 1, 0))

    def test_settypecenter(self):
        self.assertEqual(1, self.piece.get_number_of_sides(Piece.Piece.CENTER))

    def test_settypeside(self):
        self.assertEqual(2, self.piece.get_number_of_sides(Piece.Piece.SIDE))

    def test_settypeedge(self):
        self.assertEqual(3, self.piece.get_number_of_sides(Piece.Piece.EDGE))

    def test_settypenone(self):
        self.assertEqual(-1, self.piece.get_number_of_sides("kijijj"))

    def test_setcolor(self):
        self.piece.set_color(cp.RED, Piece.FRONT)
        self.assertIn(cp.RED, self.piece.colors.keys())
        self.assertEqual(Piece.FRONT, self.piece.colors.get(cp.RED))

    def test_setcolortwicewithcenterpiece(self):
        self.piece.set_color(cp.RED, Piece.FRONT)
        self.piece.set_color(cp.GREEN, Piece.BACK)
        self.assertEqual(1, len(self.piece.colors.items()))
        #self.assertEqual(Piece.FRONT, self.piece.colors.get(cp.RED))

    def test_setcolorsthricewithsidepiece(self):
        self.piece = Piece.Piece(Piece.Piece.SIDE, (0, 1, 1))
        self.piece.set_color(cp.RED, Piece.FRONT)
        self.piece.set_color(cp.GREEN, Piece.BACK)
        self.piece.set_color(cp.BLUE, Piece.UP)
        self.assertEqual(2, len(self.piece.colors.items()))
        #self.assertEqual(Piece.FRONT, self.piece.colors.get(cp.RED))

    def test_setcolorstoomanycolorswithedgepiece(self):
        self.piece = Piece.Piece(Piece.Piece.EDGE, (1, 1, 1))
        self.piece.set_color(cp.RED, Piece.FRONT)
        self.piece.set_color(cp.GREEN, Piece.BACK)
        self.piece.set_color(cp.BLUE, Piece.UP)
        self.piece.set_color(cp.YELLOW, Piece.DOWN)
        self.assertEqual(3, len(self.piece.colors.items()))

    def test_setcolorsdoesnotoverwrite(self):
        self.piece.set_color(cp.RED, Piece.FRONT)
        self.piece.set_color(cp.GREEN, Piece.BACK)
        self.assertEqual("dict_keys(['RED'])", str(self.piece.colors.keys()))
        self.assertEqual("dict_values(['FRONT'])", str(self.piece.colors.values()))

    def test_setcolorraisesexception(self):
        self.piece = Piece.Piece(Piece.Piece.EDGE, (1, 1, 1))
        self.piece.set_color(cp.RED, Piece.FRONT)
        self.assertRaises(ValueError, self.piece.set_color, cp.RED, Piece.FRONT)

    def test_checkduplicatecolornoduplicate(self):
        self.piece.set_color(cp.RED, Piece.FRONT)
        self.assertFalse(self.piece.is_dupicate_color(cp.BLUE, Piece.UP))

    def test_checkduplicatecolorwithduplicatedirection(self):
        self.piece = Piece.Piece(Piece.Piece.EDGE, (1, 1, 1))
        self.piece.set_color(cp.RED, Piece.FRONT)
        self.assertTrue(self.piece.is_dupicate_color(cp.BLUE, Piece.FRONT))

    def test_checkduplicatecolorwithduplicatecolor(self):
        self.piece = Piece.Piece(Piece.Piece.EDGE, (1, 1, 1))
        self.piece.set_color(cp.RED, Piece.FRONT)
        self.assertTrue(self.piece.is_dupicate_color(cp.RED, Piece.BACK))

    def test_allcolorsareset(self):
        self.piece.set_color(cp.RED, Piece.FRONT)
        self.assertTrue(self.piece.all_colors_are_set())

    def test_allcolorsarenotset(self):
        self.piece = Piece.Piece(Piece.Piece.EDGE, (1, 1, 1))
        self.piece.set_color(cp.RED, Piece.FRONT)
        self.assertFalse(self.piece.all_colors_are_set())

    def test_vectormatrixmultiplicationedgeCC(self):
        self.assertEqual(1, self.piece.vector_multiplication((1, 1, 1), (0, 0, 1)))
        self.assertEqual(1, self.piece.vector_multiplication((1, 1, 1), (0, 1, 0)))
        self.assertEqual(-1, self.piece.vector_multiplication((1, 1, 1), (-1, 0, 0)))

    def test_vectormatrixmultiplicationsideCC(self):
        self.assertEqual(1, self.piece.vector_multiplication((0, 1, 1), (0, 0, 1)))
        self.assertEqual(1, self.piece.vector_multiplication((0, 1, 1), (0, 1, 0)))
        self.assertEqual(0, self.piece.vector_multiplication((0, 1, 1), (-1, 0, 0)))

    def test_vectormatrixmultiplicationcenterCC(self):
        self.assertEqual(0, self.piece.vector_multiplication((0, 1, 0), (0, 0, 1)))
        self.assertEqual(1, self.piece.vector_multiplication((0, 1, 0), (0, 1, 0)))
        self.assertEqual(0, self.piece.vector_multiplication((0, 1, 0), (-1, 0, 0)))

    def test_rotateedgeCC(self):
        self.piece = Piece.Piece(Piece.Piece.EDGE, (1, 1, 1))
        self.assertEqual((1, 1, -1), self.piece.rotate([[0, 0, 1], [0, 1, 0], [-1, 0, 0]]))

    def test_rotatesideCC(self):
        self.piece = Piece.Piece(Piece.Piece.SIDE, (0, 1, 1))
        self.assertEqual((1, 1, 0), self.piece.rotate([[0, 0, 1], [0, 1, 0], [-1, 0, 0]]))


if __name__ == '__main__':
    unittest.main()
