import numpy as np
import cv2
class ImageProcessing:
    @classmethod
    def splitImage(cls,image):
        imgRegions = dict()
        height,width = np.size(image,0),np.size(image,1)
       # print(height,width)
        for i in range(0,3):
            yupperbound = int((i+1) * (height / 3))
            ylowerbound = int(yupperbound - (height / 3))
            #print("YL: ", ylowerbound, "YU: ", yupperbound)
            for j in range(0,3):
                xupperbound = int((j+1)*(width/3))
                xlowerbound = int(xupperbound-(width/3))
                #print("XL: ", xlowerbound, "XU: ", xupperbound)
                imgRegions[(i,j)] = image[ylowerbound:yupperbound,xlowerbound:xupperbound]
        cv2.imshow("Cube Section",imgRegions.get((0,0)))
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        return imgRegions

    @classmethod
    def isBlue(cls, colorstats):
        b,g,r = colorstats
        return (b > r) and (r == g) or (b == g) and (b > r) or (b > g) and (g > r) or (b > r) and (r > g)

    @classmethod
    def isGreen(cls, colorstats):
        b,g,r = colorstats
        return (g > r) and (r > b) and ((g - r) >= (.25 * r)) or (g > r) and (r == b) or (g > b) and (b > g)

    @classmethod
    def isRed(cls, colorstats):
        b, g, r = colorstats
        return (r > g) and (g == b) or (r > g) and (g > b) and ((g - b) < (.25*b)) or (r > b) and (b > g) or (r == b) and (b > g)

    @classmethod
    def isYellow(cls, colorstats): #not done
        b, g, r = colorstats
        return (g > r) and (r > b) and ((g - r) < (.25 * r)) or (g == r) and (r > b) or (r > g) and (g > b) and ((r - g) < (.25*g)) and ((g - b) >= (.25*b))

    @classmethod
    def isOrange(cls, colorstats):
        b, g, r = colorstats
        return (r > g) and (g > b) and ((r - g) >= (.25*g)) and ((g - b) >= (.25*b))

    @classmethod
    def isWhite(cls, colorstats): #not done
        b, g, r = colorstats
        return (((r-g) <= (.05*g)) and ((r-b) <= (.05*b)) and ((b-g) <= (.05*g))) and (r+b+g) >= 550

    @classmethod
    def calulatecolorstats(cls, color):
        sum = color[0] + color[1] + color[2]
        return color[0] / sum, color[1] / sum, color[2] / sum

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
    def chooseColor(cls,hue):
        if hue is None:
            return "BlANK"
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




