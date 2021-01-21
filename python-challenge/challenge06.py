# http://www.pythonchallenge.com/pc/def/channel.html

import os
import zipfile
import re

dirPath = os.path.dirname(os.path.realpath(__file__))
channelPath = "assets/channel.zip"
file = zipfile.ZipFile(os.path.join(dirPath, channelPath))

# Here, we're following the numbers again, like in challenge 4. The start is at readme.txt
# Apparently, there are zip comments for each file, so we gotta collect those in order while
# following the number trail. Printing it all out will show another ASCII art of a word.

currentNumber = 90052
comments = []
while True:
    path = os.path.join(dirPath, channelPath.format(currentNumber))
    line = file.read("{0}.txt".format(currentNumber)).decode("utf-8")

    # Reading the comments
    comments.append(file.getinfo("{0}.txt".format(currentNumber)).comment.decode("utf-8"))
    
    print(line)
    match = re.search("[nN]ext nothing is (\d+)", line)
    if match == None:
        break

    currentNumber = match.group(1)

print("".join(comments))