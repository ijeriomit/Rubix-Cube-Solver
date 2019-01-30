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
                self.assertEqual(newface[i][j], "WHITE")

    def test_saveColorCellsFace_1(self):
        newface = self.cubeface.init_face_color(self.cubeface.images[1], self.cubeface.faces[1])
        for i in range(0, 3):
            for j in range(0, 3):
                self.assertEqual(newface[i][j], "ORANGE")

    def test_saveColorCellsFace_2(self):
        newface = self.cubeface.init_face_color(self.cubeface.images[2], self.cubeface.faces[2])
        for i in range(0, 3):
            for j in range(0, 3):
                self.assertEqual(newface[i][j], "GREEN")

    def test_saveColorCellsFace_3(self):
        newface = self.cubeface.init_face_color(self.cubeface.images[3], self.cubeface.faces[3])
        for i in range(0, 3):
            for j in range(0, 3):
                self.assertEqual(newface[i][j], "RED")

    def test_saveColorCellsFace_4(self):
        newface = self.cubeface.init_face_color(self.cubeface.images[4], self.cubeface.faces[4])
        for i in range(0, 3):
            for j in range(0, 3):
                self.assertEqual(newface[i][j], "BLUE")

    def test_saveColorCellsFace_5(self):
        newface = self.cubeface.init_face_color(self.cubeface.images[5], self.cubeface.faces[5])
        for i in range(0, 3):
            for j in range(0, 3):
                self.assertEqual(newface[i][j], "YELLOW")


if __name__ == '__main__':
    unittest.main()
