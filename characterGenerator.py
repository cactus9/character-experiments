from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

import numpy as np
"""
Okay, this is how we're going to construct this dataset:
1. For every codepoint in the CJK unified block, we're going to do the following:
    Convert to character
    Write to file
    Read pixels from file
    Save to numpy array
2. With all the character datapoints in one big array, we'll use numpy.savez to save them all to 1 file
"""
def getPixelArray(i):
    #Create a new image
    img = Image.new("L",[22,23])
    #Set up the drawing API
    draw = ImageDraw.Draw(img)
    #Font location may vary on your system, change as needed
    font=ImageFont.truetype("/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc",24)
    #Draw the character, positioned properly
    draw.text((-1,-7),chr(i),font=font,fill=255)
    img.save('temp.png')

    #Read the pixels
    im = Image.open("temp.png")
    pix = im.load()
    #The order of the indices here is a bit counter-intuitive, but y has to stay the same to print out a whole row while x changes
    return [[pix[x,y] for x in range(22)] for y in range(23)]

characterArray = np.array(
    [getPixelArray(i) for i in range(19968,40944)]
)
np.savez_compressed("character_images.npz", charSet=characterArray)
