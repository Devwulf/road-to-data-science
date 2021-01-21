# http://www.pythonchallenge.com/pc/def/oxygen.html

from PIL import Image
import os

dirPath = os.path.dirname(os.path.realpath(__file__))
imgPath = "assets/oxygen.png"
filePath = os.path.join(dirPath, imgPath)

img = Image.open(filePath)
width = img.width
height = img.height

chars = []
# Go through the entire img horizontally
for i in range(0, width):
    # Since the grey blocks are at the middle of the img vertically,
    # we use height / 2
    color = img.getpixel((i, height / 2))

    # We're only looking for the grey colors
    if color[0] != color[1] != color[2]:
        break

    # Each grey block on the img is 7 pixels wide
    if i % 7 != 0:
        continue

    chars.append(chr(color[0]))

print("".join(chars))

nextLevel = [105, 110, 116, 101, 103, 114, 105, 116, 121]
print("".join([chr(num) for num in nextLevel]))