from ImageProcessing import ImageProcessing
from ColorPicker import PickColor


class CubeFace:

    def __init__(self, id):
        self.id = id
        self.colorcells = [[None for i in range(0, 3)] for j in range(0, 3)]
        self.pickColor = PickColor()
        self.imgPro = ImageProcessing()

    def saveColorCells(self, image):
        cells = self.imgPro.splitImage(image)
        for i in range(0, 3):
            for j in range(0, 3):
                self.colorcells[i][j] = self.pickColor.calculateColorinCell(cells.get((i, j)))
