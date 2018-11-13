import unittest
from src.ImageIO import ImageIO
import numpy as np
from ImageProcessing import ImageProcessing as imgPro


class MyTestCase(unittest.TestCase):

    def test_splitsimageinto9regions (self):
        self.assertEqual(len(imgPro.splitImage(ImageIO.loadImages("7", ".jpg"))), 9)

    def test_noduplicateregions(self):
        imgregions = imgPro.splitImage(ImageIO.loadImages("1", ".jpg")).values()
        seen = list()
        for x in imgregions:
            for i in seen:
                self.assertFalse(np.array_equal(x, i))
            seen.append(x)

    def test_colorisRed(self):
        self.assertEqual("RED", imgPro.chooseColor(imgPro.calculateHue((0, 0, 255))))

    def test_colorisBlue(self):
        self.assertEqual("BLUE", imgPro.chooseColor(imgPro.calculateHue((255, 0, 0))))

    def test_colorisGreen(self):
        self.assertEqual("GREEN",imgPro.chooseColor(imgPro.calculateHue((0, 255, 0))))

    def test_colorisYellow(self):
        self.assertEqual("YELLOW", imgPro.chooseColor(imgPro.calculateHue((0, 255, 255))))

    def test_colorisOrange(self):
        self.assertEqual("ORANGE", imgPro.chooseColor(imgPro.calculateHue((0, 127, 255))))

    def test_coloriswhite(self):
        self.assertTrue(imgPro.isWhite((255, 255, 255)))

    def test_blackcolor(self):
        self.assertEqual("BLANK", imgPro.chooseColor(imgPro.calculateHue((0, 0, 0))))

    def test_greenishblueisblue(self):
        self.assertEqual("BLUE", imgPro.chooseColor(imgPro.calculateHue((139, 139, 0))))

    def test_orangishredisred(self):
        self.assertEqual("RED", imgPro.chooseColor(imgPro.calculateHue((92, 115, 232))))

    def test_orangeishyellowisyellow(self):
        self.assertEqual("YELLOW", imgPro.chooseColor(imgPro.calculateHue((0, 198, 255))))


if __name__ == '__main__':
    unittest.main()
