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

    def test_colorisRedwithIsRed(self):
        self.assertTrue(imgPro.isRed((0, 0, 255)))

    def test_colorisRedwithChooseColor(self):
        self.assertEqual("RED", imgPro.chooseColor(imgPro.calculateHue((0, 0, 255))))

    def test_colorisBluewithIsBlue(self):
        self.assertTrue(imgPro.isBlue((255, 0, 0)))

    def test_colorisBluewithChooseColor(self):
        self.assertEqual(imgPro.chooseColor(imgPro.calculateHue((255, 0, 0))), "BLUE")

    def test_colorisGreenwithIsGreen(self):
        self.assertTrue(imgPro.isGreen((0, 255, 0)))

    def test_colorisGreenwithChooseColor(self):
        self.assertEqual(imgPro.chooseColor(imgPro.calculateHue((0, 255, 0))), "GREEN")

    def test_colorisYellowwithIsYellow(self):
        self.assertTrue(imgPro.isYellow((0, 255, 255)))

    def test_colorisYellowwithChooseColor(self):
        self.assertEqual(imgPro.chooseColor(imgPro.calculateHue((0, 255, 255))), "YELLOW")

    def test_colorisOrangewithIsOrange(self):
        self.assertTrue(imgPro.isOrange((0, 127, 255)))

    def test_colorisOrangewithChooseColor(self):
        self.assertEqual(imgPro.chooseColor(imgPro.calculateHue((0, 127, 255))), "ORANGE")



    def test_coloriswhite(self):
       self.assertTrue(imgPro.isWhite((255, 255, 255)))

    def test_graycolorwithChooseColor(self):
        self.assertEqual("WHITE", imgPro.chooseColor(imgPro.calculateHue((0, 0, 0))))



    def test_greenishblueisbluewithIsBlue(self):
       self.assertTrue((imgPro.isBlue((139, 139, 0))))

    def test_greenishblueisbluewithChooseColor(self):
        self.assertEqual("BLUE", imgPro.chooseColor(imgPro.calculateHue((139, 139, 0))))

#challenge
    def test_orangishredisredwithIsRed(self):
        self.assertTrue((imgPro.isRed((92, 115, 232))))

    def test_orangishredisredwithChooseColor(self): #winner
        self.assertEqual("RED", imgPro.chooseColor(imgPro.calculateHue((92, 115, 232))))

    def test_orangeishyellowisyellowwithIsYellow(self):
        self.assertTrue((imgPro.isYellow((0, 198, 255))))

    def test_orangeishyellowisyellowwithChooseColor(self): #winner
        self.assertEqual("YELLOW", imgPro.chooseColor(imgPro.calculateHue((0, 198, 255))))





   # def test_purplishblueisblue(self):
    #    self.assertTrue((imgPro.isBlue((255, 0, 143))))

    def test_calculatecolorstats(self):
        self.assertEqual(imgPro.calulatecolorstats((255, 0, 0)), (1, 0, 0))

    def test_calculatestatswithfloatingpointdecimals(self):
        stats = imgPro.calulatecolorstats((251, 42, 78))
        self.assertEqual(stats, (0.6765498652291105, 0.11320754716981132,0.21024258760107817))

if __name__ == '__main__':
    unittest.main()
