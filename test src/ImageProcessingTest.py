import unittest
from src.ImageIO import ImageIO
import numpy as np
from ImageProcessing import ImageProcessing as imgPro

class MyTestCase(unittest.TestCase):

    def test_splitsimageinto9regions (self):
        self.assertEqual(len(imgPro.splitImage(ImageIO.loadImages("7", ".jpg"))), 9)

    def test_noduplicateregions(self):
        imgRegions = imgPro.splitImage(ImageIO.loadImages("1", ".jpg")).values()
        seen = list()
        for x in imgRegions:
            for i in seen:
                self.assertFalse(np.array_equal(x,i))
            seen.append(x)
    def test_colorisred(self):
        self.assertTrue(imgPro.isRed((0, 0, 255)))

    def test_colorisblue(self):
        self.assertTrue(imgPro.isBlue((255, 0, 0)))

    def test_colorsisgreen(self):
        self.assertTrue(imgPro.isGreen((0, 255, 0)))

    def test_calculatecolorstats(self):
        self.assertEqual(imgPro.calulatecolorstats((255, 0, 0)), (1, 0, 0))

    def test_calculatestatswithfloatingpointdecimals(self):
        stats = imgPro.calulatecolorstats((251, 42, 78))
        self.assertEqual(stats, (0.6765498652291105, 0.11320754716981132,0.21024258760107817))

    def test_isbluewithcalculatestats(self):
        self.assertTrue(imgPro.isBlue(imgPro.calulatecolorstats((255, 0, 0))))

    def test_greenishblueisblue(self):
        self.assertTrue((imgPro.isBlue(imgPro.calulatecolorstats((139, 139, 0)))))

    def test_purplishblueisblue(self):
        self.assertTrue((imgPro.isBlue(imgPro.calulatecolorstats((255, 0, 143)))))



if __name__ == '__main__':
    unittest.main()
