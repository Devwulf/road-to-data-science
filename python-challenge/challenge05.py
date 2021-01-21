# http://www.pythonchallenge.com/pc/def/peak.html

import pickle
import os

dirPath = os.path.dirname(os.path.realpath(__file__))
inputPath = "assets/banner.p"

# Here, we're using pickle to unpickle (aka deserialize) a pickled (aka serialized) file
# Pickling is kinda the same as serializing to JSON, but only in specific programming langs
# like Python

file = open(os.path.join(dirPath, inputPath), "rb")
obj = pickle.load(file);
file.close()

# Once unpickled, the obj is an array of arrays, specifying the character to print to a line
# and how many times to print it. It'll draw an ASCII art showing a word

for i in obj:
    line = ""
    for j in i:
        for k in range(0, j[1]):
            line += j[0]
    print(line)