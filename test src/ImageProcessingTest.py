import unittest
from src.ImageIO import ImageIO
import numpy as np
from ImageProcessing import ImageProcessing


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.imageIO = ImageIO()
        self.imgPro = ImageProcessing()

    def test_splitsimageinto9regions(self):
        self.assertEqual(len(self.imgPro.splitImage(self.imageIO.loadImage("3", ".jpg"))), 9)

    def test_noduplicateregions(self):
        imgregions = self.imgPro.splitImage(self.imageIO.loadImage("1", ".jpg")).values()
        seen = list()
        for x in imgregions:
            for i in seen:
                self.assertFalse(np.array_equal(x, i))
            seen.append(x)


if __name__ == '__main__':
    unittest.main()
