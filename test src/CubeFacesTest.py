import unittest
from CubeFaces import CubeFaces
from ImageIO import ImageIO


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.imageIO = ImageIO()
        self.cubeface = CubeFaces()

    def test_save_image(self):
        self.cubeface.saveImage(0)
        self.assertNotEqual(None, self.cubeface.images[0])

    def test_saveColorCellsFace_0(self):
        newface = self.cubeface.init_face_color(self.imageIO.loadImage("0", ".jpg"), self.cubeface.faces[0])
        for i in range(0, 3):
            for j in range(0, 3):
                self.assertEqual(newface[i][j], "WHITE")

    def test_saveColorCellsFace_1(self):
        newface = self.cubeface.init_face_color(self.imageIO.loadImage("1", ".jpg"), self.cubeface.faces[0])
        for i in range(0, 3):
            for j in range(0, 3):
                self.assertEqual(newface[i][j], "ORANGE")

    def test_saveColorCellsFace_2(self):
        newface = self.cubeface.init_face_color(self.imageIO.loadImage("2", ".jpg"), self.cubeface.faces[0])
        for i in range(0, 3):
            for j in range(0, 3):
                self.assertEqual(newface[i][j], "GREEN")

    def test_saveColorCellsFace_3(self):
        newface = self.cubeface.init_face_color(self.imageIO.loadImage("3", ".jpg"), self.cubeface.faces[0])
        for i in range(0, 3):
            for j in range(0, 3):
                self.assertEqual(newface[i][j], "RED")

    def test_saveColorCellsFace_4(self):
        newface = self.cubeface.init_face_color(self.imageIO.loadImage("4", ".jpg"), self.cubeface.faces[0])
        for i in range(0, 3):
            for j in range(0, 3):
                self.assertEqual(newface[i][j], "BLUE")

    def test_saveColorCellsFace_5(self):
        newface = self.cubeface.init_face_color(self.imageIO.loadImage("5", ".jpg"), self.cubeface.faces[0])
        for i in range(0, 3):
            for j in range(0, 3):
                self.assertEqual(newface[i][j], "YELLOW")

    def test_init_all_faces(self):
        self.cubeface.init_all_faces()
        for k in range(0, 6):
            for j in range(0, 3):
                self.assertNotIn(None, self.cubeface.faces)

    def test_init_all_faces2(self):
        self.assertIn(None, self.cubeface.faces[0][0])


if __name__ == '__main__':
    unittest.main()
