import unittest
import Piece
import ColorPicker as cp
import Cube as cb

class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.piece = Piece.Piece(Piece.CENTER, (0, 1, 0))

    def test_settypecenter(self):
        self.assertEqual(1, self.piece.getnumberofsides(Piece.CENTER))

    def test_settypeside(self):
        self.assertEqual(2, self.piece.getnumberofsides(Piece.SIDE))

    def test_settypeedge(self):
        self.assertEqual(3, self.piece.getnumberofsides(Piece.EDGE))

    def test_settypenone(self):
        self.assertEqual(-1, self.piece.getnumberofsides("kijijj"))

    def test_setcolorwithCenterPiece(self):
        self.piece.set_color(cp.RED, cb.FRONT)
        self.assertEqual([(cp.RED, cb.FRONT)], self.piece.piececolors)

    def test_setcolorwithsidePiece(self):
        self.piece = Piece.Piece(Piece.SIDE, (1, 1, 0))
        self.piece.set_color(cp.RED, cb.FRONT)
        self.assertEqual([(cp.RED, cb.FRONT), None], self.piece.piececolors)

    def test_setcolorwithEdgePiece(self):
        self.piece = Piece.Piece(Piece.EDGE, (1, 1, 1))
        self.piece.set_color(cp.RED, cb.FRONT)
        self.assertEqual([(cp.RED, cb.FRONT), None, None], self.piece.piececolors)

    def test_setcolortwicewithcenterpiece(self):
        self.piece.set_color(cp.RED, cb.FRONT)
        self.piece.set_color(cp.GREEN, cb.BACK)
        self.assertEqual([(cp.RED, cb.FRONT)], self.piece.piececolors)

    def test_setcolorsthricewithsidepiece(self):
        self.piece = Piece.Piece(Piece.SIDE, (0, 1, 1))
        self.piece.set_color(cp.RED, cb.FRONT)
        self.piece.set_color(cp.GREEN, cb.BACK)
        self.piece.set_color(cp.BLUE, cb.UP)
        self.assertEqual([(cp.RED, cb.FRONT), (cp.GREEN, cb.BACK)], self.piece.piececolors)

    def test_setcolorstoomanycolorswithedgepiece(self):
        self.piece = Piece.Piece(Piece.EDGE, (1, 1, 1))
        self.piece.set_color(cp.RED, cb.FRONT)
        self.piece.set_color(cp.GREEN, cb.BACK)
        self.piece.set_color(cp.BLUE, cb.UP)
        self.piece.set_color(cp.YELLOW, cb.DOWN)
        self.assertEqual([(cp.RED, cb.FRONT), (cp.GREEN, cb.BACK), (cp.BLUE, cb.UP)], self.piece.piececolors)

    def test_allcolorsset(self):
        self.piece.set_color(cp.RED, cb.FRONT)
        self.assertTrue(self.piece.all_colors_are_set())

    def test_allcolorsnotset(self):
        self.assertFalse(self.piece.all_colors_are_set())


if __name__ == '__main__':
    unittest.main()
