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
    rm.show()
    (newWidth, newHeight) = rm.size
    symbols = ['@', '%', '#', 'x', '+', '=', ':', '-', '.', ' ']
    print(symbols)
    outfile = open("test.txt", "w")
    for i in range(newHeight):
        for j in range(newWidth):
            y = []
            (R, G, B) = rm.getpixel(j, i)
            brightness = rgbToBrightness((R, G, B))
            symbolIndex = int(brightness/255)
            symbol = symbols[symbolIndex]
            y = y.append(symbol)
        print(y+"\n", file=outfile)
    outfile.close()
    final = list(rm.getdata())
    return final


def rgbToBrightness(rgbband):
    (R, G, B) = rgbband
    Y = R*0.299+G*0.587+B*0.114
    return Y


def newImageSize(width, height):
    newWidth = 173
    newHeight = (height * newWidth) / width
    return (newWidth, int(newHeight))


if __name__ == '__main__':
    processImagePath("/home/rag/Pictures/New folder/_7B2zqw33q7fhb7znvtIXcbsmITo09KWg4fFQUIaEFA.jpg")
