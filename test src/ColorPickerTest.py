
import unittest
from ColorPicker import PickColor

class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.pickColor = PickColor()

    def test_colorisRed(self):
        self.assertEqual("RED", self.pickColor.chooseColor(self.pickColor.calculateHue((0, 0, 255))))

    def test_colorisBlue(self):
        self.assertEqual("BLUE", self.pickColor.chooseColor(self.pickColor.calculateHue((255, 0, 0))))

    def test_colorisGreen(self):
        self.assertEqual("GREEN", self.pickColor.chooseColor(self.pickColor.calculateHue((0, 255, 0))))

    def test_colorisYellow(self):
        self.assertEqual("YELLOW", self.pickColor.chooseColor(self.pickColor.calculateHue((0, 255, 255))))

    def test_colorisOrange(self):
        self.assertEqual("ORANGE", self.pickColor.chooseColor(self.pickColor.calculateHue((0, 127, 255))))

    def test_coloriswhite(self):
        self.assertEqual("WHITE", self.pickColor.chooseColor(self.pickColor.calculateHue((245, 250, 255))))

    def test_blackcolor(self):
        self.assertEqual("BLANK", self.pickColor.chooseColor(self.pickColor.calculateHue((0, 0, 0))))

    def test_greenishblueisblue(self):
        self.assertEqual("BLUE", self.pickColor.chooseColor(self.pickColor.calculateHue((139, 139, 0))))

    def test_orangishredisred(self):
        self.assertEqual("RED", self.pickColor.chooseColor(self.pickColor.calculateHue((92, 115, 232))))

    def test_orangeishyellowisyellow(self):
        self.assertEqual("YELLOW", self.pickColor.chooseColor(self.pickColor.calculateHue((0, 198, 255))))

    def test_iswhite(self):
        self.assertEqual(True, self.pickColor.isWhite((245, 250, 255)))

    def test_calculatecolorincell1(self):
        impro = ImageProcessing()
        imio = ImageIO()
        self.assertEqual("RED", self.pickColor.calculateColorinCell(impro.splitImage(imio.loadImage("0", ".jpg")).get((0, 0))))

    def test_calculatecolorincell2(self):
        impro = ImageProcessing()
        imio = ImageIO()
        self.assertEqual("GREEN", self.pickColor.calculateColorinCell(impro.splitImage(imio.loadImage("1", ".jpg")).get((0, 0))))


if __name__ == '__main__':
    unittest.main()
