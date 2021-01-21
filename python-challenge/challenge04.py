# http://www.pythonchallenge.com/pc/def/linkedlist.php

# Send GET requests to http://www.pythonchallenge.com/pc/def/linkedlist.php
# with one query 'nothing' equal to the number shown in the GET response
# The first 'nothing' is 12345

import urllib.request
import re

# Lots of weirdness on this challenge, just follow the printouts

url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing={0}"
currentNothing = 12345
finalNothing = 66831
while True:
    with urllib.request.urlopen(url.format(currentNothing)) as response:
        html = response.read().decode("utf-8")
        print(html)
        match = re.search("[nN]ext nothing is (\d+)", html)
        if match == None:
            break

        currentNothing = match.group(1)