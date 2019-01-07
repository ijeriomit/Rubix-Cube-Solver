from ImageProcessing import ImageProcessing
from ColorPicker import PickColor


class ColorCells:

    def __init__(self):
        self.colorcells = [[None for _ in range(0, 3)] for _ in range(0, 3)]
        self.pickColor = PickColor()
        self.imgPro = ImageProcessing()

    def saveColorCells(self, image):
        cells = self.imgPro.splitImage(image)
        for i in range(0, 3):
            for j in range(0, 3):
                self.colorcells[i][j] = self.pickColor.calculateColorinCell(cells.get((i, j)))
