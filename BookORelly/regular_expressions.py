#https://developers.google.com/edu/python/regular-expressions
#\w -- (lowercase w) matches a "word" character: a letter or digit or underbar [a-zA-Z0-9_].

import re

str = 'an example word:cat!!'
match = re.search(r'word:\w\w\w', str)
# If-statement after search() tests if it succeeded
if match:
    print ('found', match.group()) ## 'found word:cat'
else:
    print ('did not find')