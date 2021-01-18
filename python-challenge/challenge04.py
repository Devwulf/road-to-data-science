# Send GET requests to http://www.pythonchallenge.com/pc/def/linkedlist.php
# with one query 'nothing' equal to the number shown in the GET response
# The first 'nothing' is 12345

import urllib.request
import re

# Lots of weirdness on this challenge, just follow the printouts

url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing={0}"
currentNothing = 63579
for i in range(0, 400):
    with urllib.request.urlopen(url.format(currentNothing)) as response:
        html = response.read().decode("utf-8")
        print(html)
        match = re.search("[0-9]+", html)
        currentNothing = match.group()