
#!/usr/bin/env python

# sys imports
import subprocess as subprocess
import os
import dateutil
from datetime import datetime
import time


"""

###############################################################################

The point of this is just to create spelling tests for words

I should be able to be tested on a word and see if it's spelt correctly

Have multiple words apprear and choose the correct one from A,B,C.

List of misspelt words from wikipedia:

https://en.wikipedia.org/wiki/Commonly_misspelled_English_words

-------------------------------------------------------------------------------

Spelling words will be stored in a separate file.

From here :
http://www.oxforddictionaries.com/words/common-misspellings

I quite like this format

---------------------------------------------------------------
| Correct spelling --- Spelling Advice --- Common misspelling |
---------------------------------------------------------------

I might also add a brief meaning to the word, and a link to look it up in an
online dictionary? (Would I want / need to add more than this in future? Should
I be able to? Is this already a little overkill?)

I would also like to be able to keep track of words that I commonly misspell...
So that when I go through the spelliing test if I get a word wrong it's flagged
up.

What's the best way to store the information? Should each word be an object?
This would make sense I think in terms of them being extendible and having
data... but maybe I could just a dictionary for them instead.

I could have a dictionary of words

words = {
    'word' = "absence",
    'misspelling' = "absense, absance",
}


words = {
    'absence':
    ['absense', 'absance']
    }


words = {'absence': {'score': 10, 'misspellings': ['x',

               'y']}}  [15:37]


-------------------------------------------------------------------------------

I would also like to have something similar for grammar terms, so that I have
something that would prompt usage of a verb a noun, pronoun, contractions etc
etc... Though this script is just for spelling.

"""
