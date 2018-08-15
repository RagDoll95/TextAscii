from PIL import Image
import pdb
import sys


def processImagePath(path):
    im = Image.open(path)
    im.load()
    im.show()
    (width, height) = im.size
    print(path)
    x = list(im.getdata())
    y = []
    for line in x:
        y.append(rgbToBrightness(line))
    rm = im.resize(newImageSize(width, height))
    rm.open()
    rm.show()
    n = width
    final = [y[i * n:(i + 1) * n] for i in range((len(y) + n - 1) // n )]
    return final


def newImageSize(width, height):
    newWidth = 173
    newHeight = (height * width) / newWidth
    return (newWidth, int(newHeight))


def rgbToBrightness(rgbband):
    (R, G, B) = rgbband
    Y = (R+R+B+G+G+G)/6
    return Y


if __name__ == '__main__':
    outfile = open("test.txt", "w")
    y = processImagePath("/home/rag/Pictures/New folder/_7B2zqw33q7fhb7znvtIXcbsmITo09KWg4fFQUIaEFA.jpg")
    for line in y:
        print(line, file=outfile)
    outfile.close()
