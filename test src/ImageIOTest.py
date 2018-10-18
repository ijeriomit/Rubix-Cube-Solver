import unittest
from src.ImageIO import ImageIO


class ImageIOTest(unittest.TestCase):

    def test_loadImage(self):
        self.assertNotEqual(ImageIO.loadImages("1",".jpg"), None)

    def test_FileTypeIsValid(self):
        self.assertTrue(ImageIO.checkValidImageFormat(".jpg"))

    def test_FileTypoisInvalid(self):
        self.assertFalse((ImageIO.checkValidImageFormat("jepeo")))

if __name__ == '__main__':
    unittest.main()
