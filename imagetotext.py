from PIL import Image
import pdb
import sys


def processImagePath(path):
    im = Image.open(path)
    im.load()
    (width, height) = im.size
    print(path)
    x = list(im.getdata())
    y = []
    for line in x:
        y.append(rgbToBrightness(line))
    n = width
    final = [y[i * n:(i + 1) * n] for i in range((len(y) + n - 1) // n )]
    return final


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
