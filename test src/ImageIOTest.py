import unittest
from src.ImageIO import ImageIO


class ImageIOTest(unittest.TestCase):


    def test_loadImage(self):
        self.assertEqual(len(ImageIO.loadImages()), 6)


if __name__ == '__main__':
    unittest.main()
