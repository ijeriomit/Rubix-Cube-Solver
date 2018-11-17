import random
import numpy as np
import cv2


def displayImage(windowname, image):
    cv2.imshow(windowname, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


class ImageProcessing:

    @classmethod
    def splitImageIntoRegions(cls, image):
        imgregions = dict()
        height, width = np.size(image, 0), np.size(image, 1)
        for i in range(0, 3):
            yupperbound = int((i+1) * (height / 3))
            ylowerbound = int(yupperbound - (height / 3))
            for j in range(0, 3):
                xupperbound = int((j + 1) * (width / 3))
                xlowerbound = int(xupperbound-(width / 3))
                imgregions[(i, j)] = image[ylowerbound:yupperbound, xlowerbound:xupperbound]
        return imgregions


    @classmethod
    def isWhite(cls, colorstats):
        b, g, r = colorstats
        return (((r-g) <= (.05*g)) and ((r-b) <= (.05*b)) and ((b-g) <= (.05*g))) and (r+b+g) >= 550

    @classmethod
    def calculateHue(cls, pixel):
        b, g, r = pixel
        if r == g == b:
            return None
        if cls.isWhite(pixel):
            return -1
        elif (r >= g) and (g >= b):
            hue = 60 * ((g - b)/(r - b))
        elif (g > r) and (r >= b):
            hue = 60 * (2 - ((r - b)/(g - b)))
        elif (g >= b) and (b > r):
            hue = 60 * (2 + ((b - r)/(g - r)))
        elif (b > g) and (g > r):
            hue = 60 * (4 - ((g - r)/(b - r)))
        elif (b > r) and (r >= g):
            hue = 60 * (4 + ((r - g)/(b - g)))
        elif (r >= b) and (b > g):
            hue = 60 * (6 - ((b - g)/(r - g)))
        return hue

    @classmethod
    def chooseColor(cls, hue):
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

