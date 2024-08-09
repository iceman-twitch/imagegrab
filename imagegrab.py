import random
import sys
from PIL import Image, ImageDraw, ImageGrab
import numpy


pil_img = ImageGrab.grab()
im = pil_img
walnut = Image.open ('image.png')
samples = 5
samples = int (samples)

pixels = []
while len (pixels) < samples:
    x = random.randint (0, walnut.size [0] - 1)
    y = random.randint (0, walnut.size [1] - 1)
    pixel = walnut.getpixel ( (x, y) )
    if pixel [-1] > 200:
        pixels.append ( ( (x, y), pixel [:-1] ) )

def diff (a, b):
    return sum ( (a - b) ** 2 for a, b in zip (a, b) )

best = []

for x in range (im.size [0] ):
    for y in range (im.size [1] ):
        d = 0
        for coor, pixel in pixels:
            try:
                ipixel = im.getpixel ( (x + coor [0], y + coor [1] ) )
                d += diff (ipixel, pixel)
            except IndexError:
                d += 256 ** 2 * 3
        best.append ( (d, x, y) )
        best.sort (key = lambda x: x [0] )
        best = best [:3]

x, y = best[1:]
# x = x + ( walnut.size[0] / 2 )
# y = y + ( walnut.size[1] / 2 )
print( str(x[0]) + " " + str(y[0]) )
# draw = ImageDraw.Draw (im)
# for best in best:
    # x, y = best [1:]
    # draw.rectangle ( (x, y, x + walnut.size [0], y + walnut.size [1] ), outline = 'red')
# im.save ('out.png')