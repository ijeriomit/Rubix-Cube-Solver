import unittest
from CubeFaces import CubeFaces
from Images import Cube_1


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.cubeface = CubeFaces(Cube_1)

    def test_save_image(self):
        self.assertNotEqual(None, self.cubeface.images[0].any())

    def test_checkValidFormat_png(self):
        self.assertTrue(self.cubeface.checkValidImageFormat("file.png"))

    def test_checkValidFormat_jpg(self):
        self.assertTrue(self.cubeface.checkValidImageFormat("file.jpg"))

    def test_checkValidFormat_tga(self):
        self.assertTrue(self.cubeface.checkValidImageFormat("file.tga"))

    def test_checkInvalidFormat(self):
        self.assertFalse(self.cubeface.checkValidImageFormat("file.iojjij"))

    def test_loadimages1(self):
        images = self.cubeface.load_images(Cube_1)
        for i in images:
            self.assertFalse(i.any() is None)

    def test_loadimages2(self):
        self.assertEqual(6, len(self.cubeface.load_images(Cube_1)))

    def test_init_all_faces(self):
        self.cubeface.init_all_faces()
        for k in range(0, 6):
            for j in range(0, 3):
                self.assertNotIn(None, self.cubeface.faces)

    def test_init_all_faces2(self):
        self.assertIn(None, self.cubeface.faces[0][0])

    def test_saveColorCellsFace_0(self):
        newface = self.cubeface.init_face_color(self.cubeface.images[0], self.cubeface.faces[0])
        for i in range(0, 3):
            for j in range(0, 3):
                self.assertEqual(newface[i][j], "W")

    def test_saveColorCellsFace_1(self):
        newface = self.cubeface.init_face_color(self.cubeface.images[1], self.cubeface.faces[1])
        for i in range(0, 3):
            for j in range(0, 3):
                self.assertEqual(newface[i][j], "O")

    def test_saveColorCellsFace_2(self):
        newface = self.cubeface.init_face_color(self.cubeface.images[2], self.cubeface.faces[2])
        for i in range(0, 3):
            for j in range(0, 3):
                self.assertEqual(newface[i][j], "G")

    def test_saveColorCellsFace_3(self):
        newface = self.cubeface.init_face_color(self.cubeface.images[3], self.cubeface.faces[3])
        for i in range(0, 3):
            for j in range(0, 3):
                self.assertEqual(newface[i][j], "R")

    def test_saveColorCellsFace_4(self):
        newface = self.cubeface.init_face_color(self.cubeface.images[4], self.cubeface.faces[4])
        for i in range(0, 3):
            for j in range(0, 3):
                self.assertEqual(newface[i][j], "B")

    def test_saveColorCellsFace_5(self):
        newface = self.cubeface.init_face_color(self.cubeface.images[5], self.cubeface.faces[5])
        for i in range(0, 3):
            for j in range(0, 3):
                self.assertEqual(newface[i][j], "Y")

    def test_create_cube_string_1(self):
        self.cubeface.init_all_faces()
        self.assertEqual("WWWWWWWWW", ''.join(
            self.cubeface.create_string_from_face(self.cubeface.faces[0], self.cubeface.up_pos_matrix, self.cubeface.cube_str_list)))

    def test_create_cube_string_2(self):
        self.cubeface.init_all_faces()
        self.assertEqual("OOOOOOOOO", ''.join(
            self.cubeface.create_string_from_face(self.cubeface.faces[1], self.cubeface.front_pos_matrix, self.cubeface.cube_str_list)))

    def test_create_cube_string_3(self):
        self.cubeface.init_all_faces()
        self.assertEqual("GGGGGGGGG", ''.join(
            self.cubeface.create_string_from_face(self.cubeface.faces[2], self.cubeface.right_pos_matrix, self.cubeface.cube_str_list)))

    def test_create_cube_string_4(self):
        self.cubeface.init_all_faces()
        self.assertEqual("RRRRRRRRR", ''.join(
            self.cubeface.create_string_from_face(self.cubeface.faces[3], self.cubeface.back_pos_matrix, self.cubeface.cube_str_list)))

    def test_create_cube_string_5(self):
        self.cubeface.init_all_faces()
        self.assertEqual("BBBBBBBBB", ''.join(
            self.cubeface.create_string_from_face(self.cubeface.faces[4], self.cubeface.left_pos_matrix, self.cubeface.cube_str_list)))

    def test_create_cube_string_6(self):
        self.cubeface.init_all_faces()
        self.assertEqual("YYYYYYYYY", ''.join(
            self.cubeface.create_string_from_face(self.cubeface.faces[5], self.cubeface.down_pos_matrix, self.cubeface.cube_str_list)))

    def test_create_cube_string_all_values_equal_and_same(self):
        self.cubeface.init_all_faces()
        cubestr = self.cubeface.create_cube_string()
        temp = [cubestr.count('R'), cubestr.count('O'), cubestr.count('G'),
                cubestr.count('B'), cubestr.count('W'), cubestr.count('Y')]
        self.assertEqual(1, len(set(temp)))
        self.assertEqual(9, temp[0])

if __name__ == '__main__':
    unittest.main()
