import unittest
from src.ImageIO import ImageIO


class ImageIOTest(unittest.TestCase):

    def setUp(self):
        self.imageIO = ImageIO()

    def test_loadValidImage(self):
        self.assertNotEqual(self.imageIO.loadImage("1", ".jpg").all(), None)

    def test_loadInvalidImageName(self):
        self.assertRaises(FileNotFoundError, self.imageIO.loadImage, "10", ".jpg")

    def test_loadInvalidFileType(self):
        self.assertRaises(FileNotFoundError, self.imageIO.loadImage, "1", ".jpggh")

    def test_checkValidFormat(self):
        try:
            self.imageIO.checkValidImageFormat(".png")
        except FileNotFoundError:
            self.fail("function raised and exception")
            
    def test_checkInvalidFormat(self):
        self.assertRaises(FileNotFoundError, self.imageIO.checkValidImageFormat, ".ihjh")



if __name__ == '__main__':
    unittest.main()
