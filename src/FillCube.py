import random


class FillCube:

    @classmethod
    def calculateColortallyinCell(cls, cell):
        height, width = cell.shape()
        colortally = dict()
        colortally["BLANK"], colortally["WHITE"], colortally["RED"], colortally["ORANGE"], \
            colortally["YELLOW"], colortally["GREEN"], colortally["BLUE"] = [0, 0, 0, 0, 0, 0, 0]
        for i in range(0, height):
            for j in range(0, width):
                colortally[(cls.chooseColor(cls.calculateHue(cell[i, j])))] += 1
        return colortally

    @classmethod
    def findMaxColorInTally(cls, colortally):
        maxval = max(colortally.values())
        regioncolors = list()
        regioncolors.append([key for key in colortally.keys() if colortally[key] == maxval])
        return regioncolors

    @classmethod
    def getCellColor(cls, region):
        return random.choice(cls.findMaxColorInTally(cls.calculateColorTally(region)))
