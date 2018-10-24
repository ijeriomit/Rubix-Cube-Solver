import unittest
from src.ImageIO import ImageIO


class ImageIOTest(unittest.TestCase):

    def test_loadValidImage(self):
        self.assertNotEqual(ImageIO.loadImages("1",".jpg").all(), None)
    def test_loadInvalidImage(self):
        self.assertEqual(ImageIO.loadImages("10",".jjppg"), None)

    def test_FileTypeIsValid(self):
        self.assertTrue(ImageIO.checkValidImageFormat(".jpg"))

    def test_FileTypeisInvalid(self):
        self.assertFalse((ImageIO.checkValidImageFormat("jepeo")))

if __name__ == '__main__':
    unittest.main()
