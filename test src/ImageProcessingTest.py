import unittest
from src.ImageIO import ImageIO
import numpy as np
from ImageProcessing import ImageProcessing as imgPro

class MyTestCase(unittest.TestCase):

    def test_splitsimageinto9regions (self):
        self.assertEqual(len(imgPro.splitImage(ImageIO.loadImages("7", ".jpg"))), 9)

    def test_noduplicateregions(self):
        imgRegions = imgPro.splitImage(ImageIO.loadImages("1",".jpg")).values()
        seen = list()
        for x in imgRegions:
            for i in seen:
                self.assertFalse(np.array_equal(x,i))
            seen.append(x)

if __name__ == '__main__':
    unittest.main()
