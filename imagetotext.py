from PIL import Image
import sys

def processImagePath(path):
    im = Image.open(path)
    im.rotate(45).show()
    print(path)
