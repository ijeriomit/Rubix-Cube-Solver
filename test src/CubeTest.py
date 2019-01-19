import unittest
import Cube
from CubeFaces import CubeFaces
import ColorPicker as cp


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.cf = CubeFaces()
        self.cf.FillCubeMatrix()
        self.cube = Cube.Cube(self.cf.cubematrix)

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
        face = self.cube.get_face_by_ypos(1)
        self.cube.rotate_face(self.cube.U)
        self.check_duplicates(face)

    def test_rotate_face_Ui_noduplicates(self):
        face = self.cube.get_face_by_ypos(1)
        self.cube.rotate_face(self.cube.Ui)
        self.check_duplicates(face)

    def test_rotate_face_D_noduplicates(self):
        face = self.cube.get_face_by_ypos(-1)
        self.cube.rotate_face(self.cube.D)
        self.check_duplicates(face)

    def test_rotate_face_Di_noduplicates(self):
        face = self.cube.get_face_by_ypos(-1)
        self.cube.rotate_face(self.cube.Di)
        self.check_duplicates(face)

    def test_rotate_face_E_noduplicates(self):
        face = self.cube.get_face_by_ypos(0)
        self.cube.rotate_face(self.cube.E)
        self.check_duplicates(face)

    def test_rotate_face_Ei_noduplicates(self):
        face = self.cube.get_face_by_ypos(0)
        self.cube.rotate_face(self.cube.Ei)
        self.check_duplicates(face)

    def test_rotate_face_R_noduplicates(self):
        face = self.cube.get_face_by_xpos(1)
        self.cube.rotate_face(self.cube.R)
        self.check_duplicates(face)

    def test_rotate_face_Ri_noduplicates(self):
        face = self.cube.get_face_by_xpos(1)
        self.cube.rotate_face(self.cube.Ri)
        self.check_duplicates(face)

    def test_rotate_face_M_noduplicates(self):
        face = self.cube.get_face_by_xpos(0)
        self.cube.rotate_face(self.cube.M)
        self.check_duplicates(face)

    def test_rotate_face_Mi_noduplicates(self):
        face = self.cube.get_face_by_xpos(0)
        self.cube.rotate_face(self.cube.Mi)
        self.check_duplicates(face)

    def test_rotate_face_L_noduplicates(self):
        face = self.cube.get_face_by_xpos(-1)
        self.cube.rotate_face(self.cube.L)
        self.check_duplicates(face)

    def test_rotate_face_Li_noduplicates(self):
        face = self.cube.get_face_by_xpos(-1)
        self.cube.rotate_face(self.cube.Li)
        self.check_duplicates(face)

    def test_rotate_face_F_noduplicates(self):
        face = self.cube.get_face_by_zpos(1)
        self.cube.rotate_face(self.cube.F)
        self.check_duplicates(face)

    def test_rotate_face_Fi_noduplicates(self):
        face = self.cube.get_face_by_zpos(1)
        self.cube.rotate_face(self.cube.Fi)
        self.check_duplicates(face)

    def test_rotate_face_S_noduplicates(self):
        face = self.cube.get_face_by_zpos(0)
        self.cube.rotate_face(self.cube.S)
        self.check_duplicates(face)

    def test_rotate_face_Si_noduplicates(self):
        face = self.cube.get_face_by_zpos(0)
        self.cube.rotate_face(self.cube.Si)
        self.check_duplicates(face)

    def test_rotate_face_B_noduplicates(self):
        face = self.cube.get_face_by_zpos(-1)
        self.cube.rotate_face(self.cube.B)
        self.check_duplicates(face)

    def test_rotate_face_Bi_noduplicates(self):
        face = self.cube.get_face_by_zpos(-1)
        self.cube.rotate_face(self.cube.Bi)
        self.check_duplicates(face)

    def check_duplicates(self, face):
        dup = []
        for i in face:
            self.assertTrue(i.pos not in dup)
            dup.append(i.pos)


if __name__ == '__main__':
    unittest.main()
