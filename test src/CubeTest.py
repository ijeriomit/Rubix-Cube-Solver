import unittest
import Cube
from CubeFaces import CubeFaces
import ColorPicker as cp
import Piece
from collections import Counter


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.cf = CubeFaces()
        self.cf.init_all_faces()
        self.cube = Cube.Cube(self.cf.faces)

    def test_getpiece(self):
        self.assertEqual(3, self.cube.get_piece((1, 1, 1)).numofsides)

    def test_getpiecethatdoesntexist(self):
        self.assertEqual(None, self.cube.get_piece((2, 1, 1)))

    def test_setpiececolors(self):
        for piece in self.cube.cubepieces:
            self.assertNotIn(None, piece.colors)

    def test_setpieccolorswithedges(self):
        self.assertIn((cp.WHITE, "UP"), self.cube.edges[0].colors.items())
        self.assertIn((cp.GREEN, "RIGHT"), self.cube.edges[0].colors.items())
        self.assertIn((cp.ORANGE, "FRONT"), self.cube.edges[0].colors.items())

    def test_get_pieces_by_xpos_length(self):
        self.assertEqual(9, len(self.cube.get_face_by_xpos(1)))

    def test_get_pieces_by_xpos_value(self):
        newlist = self.cube.get_face_by_xpos(1)
        self.assertTrue(all(i.pos[0] == 1 for i in newlist))

    def test_get_pieces_by_ypos_value(self):
        newlist = self.cube.get_face_by_ypos(0)
        self.assertTrue(all(i.pos[1] == 0 for i in newlist))

    def test_get_pieces_by_zpos_value(self):
        newlist = self.cube.get_face_by_zpos(-1)
        self.assertTrue(all(i.pos[2] == -1 for i in newlist))

    def test_rotate_face_U_noduplicates(self):
        self.check_duplicates(self.cube.U())

    def test_rotate_face_Ui_noduplicates(self):
        self.check_duplicates(self.cube.Ui())

    def test_rotate_face_D_noduplicates(self):
        self.check_duplicates(self.cube.D())

    def test_rotate_face_Di_noduplicates(self):
        self.check_duplicates(self.cube.Di())

    def test_rotate_face_E_noduplicates(self):
        self.check_duplicates(self.cube.E())

    def test_rotate_face_Ei_noduplicates(self):
        self.check_duplicates(self.cube.Ei())

    def test_rotate_face_R_noduplicates(self):
        self.check_duplicates(self.cube.R())

    def test_rotate_face_Ri_noduplicates(self):
        self.check_duplicates(self.cube.Ri())

    def test_rotate_face_M_noduplicates(self):
        self.check_duplicates(self.cube.M())

    def test_rotate_face_Mi_noduplicates(self):
        self.check_duplicates(self.cube.Mi())

    def test_rotate_face_L_noduplicates(self):
        self.check_duplicates(self.cube.L())

    def test_rotate_face_Li_noduplicates(self):
        self.check_duplicates(self.cube.Li())

    def test_rotate_face_F_noduplicates(self):
        self.check_duplicates(self.cube.F())

    def test_rotate_face_Fi_noduplicates(self):
        self.check_duplicates(self.cube.Fi())

    def test_rotate_face_S_noduplicates(self):
        self.check_duplicates(self.cube.S())

    def test_rotate_face_Si_noduplicates(self):
        self.check_duplicates(self.cube.Si())

    def test_rotate_face_B_noduplicates(self):
        self.check_duplicates(self.cube.B())

    def test_rotate_face_Bi_noduplicates(self):
        self.check_duplicates(self.cube.Bi())

    def test_U_valid_num_of_directions(self):
        count = Counter(self.count_num_of_directions(self.cube.U()))
        self.assertIn((3, 4), count.items())
        self.assertIn((9, 1), count.items())

    def test_Ui_valid_num_of_directions(self):
        count = Counter(self.count_num_of_directions(self.cube.Ui()))
        self.assertIn((3, 4), count.items())
        self.assertIn((9, 1), count.items())

    def test_D_valid_num_of_directions(self):
        count = Counter(self.count_num_of_directions(self.cube.D()))
        self.assertIn((3, 4), count.items())
        self.assertIn((9, 1), count.items())

    def test_Di_valid_num_of_directions(self):
        count = Counter(self.count_num_of_directions(self.cube.Di()))
        self.assertIn((3, 4), count.items())
        self.assertIn((9, 1), count.items())

    def test_E_valid_num_of_directions(self):
        count = Counter(self.count_num_of_directions(self.cube.E()))
        self.assertIn((3, 4), count.items())

    def test_Ei_valid_num_of_directions(self):
        count = Counter(self.count_num_of_directions(self.cube.Ei()))
        self.assertIn((3, 4), count.items())

    def test_R_valid_num_of_directions(self):
        count = Counter(self.count_num_of_directions(self.cube.R()))
        self.assertIn((3, 4), count.items())
        self.assertIn((9, 1), count.items())

    def test_Ri_valid_num_of_directions(self):
        count = Counter(self.count_num_of_directions(self.cube.Ri()))
        self.assertIn((3, 4), count.items())
        self.assertIn((9, 1), count.items())

    def test_L_valid_num_of_directions(self):
        count = Counter(self.count_num_of_directions(self.cube.L()))
        self.assertIn((3, 4), count.items())
        self.assertIn((9, 1), count.items())

    def test_Li_valid_num_of_directions(self):
        count = Counter(self.count_num_of_directions(self.cube.Li()))
        self.assertIn((3, 4), count.items())
        self.assertIn((9, 1), count.items())

    def test_M_valid_num_of_directions(self):
        count = Counter(self.count_num_of_directions(self.cube.M()))
        self.assertIn((3, 4), count.items())

    def test_Mi_valid_num_of_directions(self):
        count = Counter(self.count_num_of_directions(self.cube.Mi()))
        self.assertIn((3, 4), count.items())

    def test_F_valid_num_of_directions(self):
        count = Counter(self.count_num_of_directions(self.cube.F()))
        self.assertIn((3, 4), count.items())
        self.assertIn((9, 1), count.items())

    def test_Fi_valid_num_of_directions(self):
        count = Counter(self.count_num_of_directions(self.cube.Fi()))
        self.assertIn((3, 4), count.items())
        self.assertIn((9, 1), count.items())

    def test_B_valid_num_of_directions(self):
        count = Counter(self.count_num_of_directions(self.cube.B()))
        self.assertIn((3, 4), count.items())
        self.assertIn((9, 1), count.items())

    def test_Bi_valid_num_of_directions(self):
        count = Counter(self.count_num_of_directions(self.cube.Bi()))
        self.assertIn((3, 4), count.items())
        self.assertIn((9, 1), count.items())

    def test_S_valid_num_of_directions(self):
        count = Counter(self.count_num_of_directions(self.cube.S()))
        self.assertIn((3, 4), count.items())

    def test_Si_valid_num_of_directions(self):
        count = Counter(self.count_num_of_directions(self.cube.Si()))
        self.assertIn((3, 4), count.items())

    def check_duplicates(self, face):
        dup = []
        for i in face:
            self.assertTrue(i.pos not in dup)
            dup.append(i.pos)

    def count_num_of_directions(self, pieces):
        counter = dict()
        piece: Piece.Piece
        for piece in pieces:
            for j in piece.colors.values():
                if j not in counter.keys():
                    counter[j] = 1
                else:
                    counter[j] += 1
        return counter.values()


if __name__ == '__main__':
    unittest.main()
