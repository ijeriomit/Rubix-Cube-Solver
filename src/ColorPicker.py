import numpy as np

class PickColor:

    def calculateColorinCell(self, cell):
        height, width = np.size(cell, 0), np.size(cell, 1)
        colortally = dict()
        colortally["BLANK"], colortally["WHITE"], colortally["RED"], colortally["ORANGE"], \
            colortally["YELLOW"], colortally["GREEN"], colortally["BLUE"] = [0, 0, 0, 0, 0, 0, 0]
        for i in range(0, height):
            for j in range(0, width):
                colortally[(self.chooseColor(self.calculateHue(cell[i, j])))] += 1
        return self.findMaxColorInTally(colortally)

    def findMaxColorInTally(self, colortally):
        maxval = max(colortally.values())
        cellcolor = ([key for key in colortally.keys() if colortally[key] == maxval])
        return cellcolor

    def isWhite(self, pixel):
        return self.calculateLuminace(pixel) >= .90


    def calculateLuminace(self, pixel):
        r, g, b = (pixel[0] / 255, pixel[1] / 255, pixel[2] / 255)
        #print((max(r, g, b) + min(r, g, b))/2)
        return (max(r, g, b) + min(r, g, b))/2

    def calculateHue(self, pixel):
        b, g, r = pixel
        if r == g == b:
            if self.isWhite(pixel):
                return -1
            return None
        elif self.isWhite(pixel):
            return -1
        elif (r >= g) and (g >= b):
            hue = 60 * ((g - b) / (r - b))
        elif (g > r) and (r >= b):
            hue = 60 * (2 - ((r - b) / (g - b)))
        elif (g >= b) and (b > r):
            hue = 60 * (2 + ((b - r) / (g - r)))
        elif (b > g) and (g > r):
            hue = 60 * (4 - ((g - r) / (b - r)))
        elif (b > r) and (r >= g):
            hue = 60 * (4 + ((r - g) / (b - g)))
        elif (r >= b) and (b > g):
            hue = 60 * (6 - ((b - g) / (r - g)))
        return hue

    def chooseColor(self, hue):
        if hue is None:
            return "BLANK"
        elif hue == -1:
            return "WHITE"
        elif hue >= 320 or hue <= 10:
            return "RED"
        elif 10 < hue <= 45:
            return "ORANGE"
        elif 45 < hue <= 60:
            return "YELLOW"
        elif 60 < hue <= 169:
            return "GREEN"
        elif 169 < hue <= 320:
            return "BLUE"
        else:
            return "BlANK"
