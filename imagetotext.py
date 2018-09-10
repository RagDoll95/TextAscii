from PIL import Image
import pdb
import sys
import math


# Take path to image, resize it and get all
# the rgb values for each pixel.
def processImagePath(path):
    im = Image.open(path)
    im.load()
    (width, height) = im.size
    rm = im.resize(newImageSize(width, height))
    (newWidth, newHeight) = rm.size
    divisor = calculateDivisor(rm.getextrema())
    symbols = ['@', '%', '#', 'x', '+', '=', ':', '-', '.', ' ']
    print(symbols)
    outfile = open("test.txt", "w")
    z = []
    for i in range(newHeight):
        for j in range(newWidth):
            (R, G, B) = rm.getpixel((j, i))
            brightness = rgbToBrightness((R, G, B))
            symbolIndex = int(brightness/divisor)
            z.append(brightness)
            symbol = symbols[symbolIndex]
            print(symbol, end="", file=outfile)
        print("\n", file=outfile)
    print(max(z))
    print(min(z))
    print(newWidth)
    print(newHeight)
    outfile.close()


def rgbToBrightness(rgbband):
    (R, G, B) = rgbband
    Y = R*0.299+G*0.587+B*0.114
    return Y


def newImageSize(width, height):
    newWidth = 173
    newHeight = (height * newWidth) / width
    return (newWidth, int(newHeight))


def calculateDivisor(nestedtuple):
    max = (nestedtuple[0][0], nestedtuple[1][0], nestedtuple[2][0])
    min = (nestedtuple[0][1], nestedtuple[1][1], nestedtuple[2][1])
    divisor = (rgbToBrightness(max)-rgbToBrightness(min))/10
    return math.ceil(abs(divisor))

if __name__ == '__main__':
    processImagePath("/home/rag/Pictures/New folder/_7B2zqw33q7fhb7znvtIXcbsmITo09KWg4fFQUIaEFA.jpg")
