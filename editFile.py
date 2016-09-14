#!/usr/bin/env python

# sys imports
import subprocess as subprocess
import os
import dateutil
from datetime import datetime
import time


"""

###############################################################################


This file is just for the creating the json


###############################################################################



read file in line by line

Convert :

aggressive % agressive

To

{'aggressive': {'misspellings': [agressive], 'misspellings_count':0}}

And

allegiance % allegaince, allegience, alegiance


To

{'allegiance': {'misspellings': ['allegaince', 'allegience', 'alegiance'] 'misspellings_count':0}}

for each word:

- read line
- split line on % sign
- UP TO THE % SIGN = key
- After the % sign = misspellings > split on commas
- add count = 0 to all
- wrap everything in {{}} to convert to json format

"""

with open("./wikipage.txt") as f:
    content = f.readlines()



def stringFormat(s):
    # this is the format that I want the string to be in
    word = s[0]
    misspellings = s[1].split(',')
    return "{{'{}': {{'misspellings': {}, 'misspellings_count': 0}}}}".format(
        word,misspellings)

wordsForJsonFile = []

for i in content:
    # I don't want / need new line characters
    i = i.replace('\n', '')
    j = i.split("%")
    # only interested in arrays that contain multiple values
    if len(j) > 1:
        wordsForJsonFile.append(stringFormat(j))

# with open("myJson.json") as
