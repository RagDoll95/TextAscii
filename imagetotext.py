from PIL import Image
import pdb
import sys


# Take path to image, resize it and get all
# the rgb values for each pixel.
def processImagePath(path):
    im = Image.open(path)
    im.load()
    (width, height) = im.size
    rm = im.resize(newImageSize(width, height))
    (newWidth, newHeight) = rm.size
    print(rm.getextrema())

    symbols = ['@', '%', '#', 'x', '+', '=', ':', '-', '.', ' ']
    print(symbols)
    outfile = open("test.txt", "w")
    z = []
#    for i in range(newHeight):
#        for j in range(newWidth):
#            (R, G, B) = rm.getpixel((j, i))
#            brightness = rgbToBrightness((R, G, B))
#            symbolIndex = int(brightness/25)
#            z.append(brightness)
#            symbol = symbols[symbolIndex]
#            print(symbol, end="", file=outfile)
#        print("\n", file=outfile)
#    print(max(z))
#    print(min(z))
#    print(newWidth)
#    print(newHeight)
#    outfile.close()


def rgbToBrightness(rgbband):
    (R, G, B) = rgbband
    Y = R*0.299+G*0.587+B*0.114
    return Y


def newImageSize(width, height):
    newWidth = 173
    newHeight = (height * newWidth) / width
    return (newWidth, int(newHeight))


def calculateDivisor(nestedtuple):
    pass

if __name__ == '__main__':
    processImagePath("/home/rag/Pictures/New folder/_7B2zqw33q7fhb7znvtIXcbsmITo09KWg4fFQUIaEFA.jpg")
