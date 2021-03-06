"""
forurl.py

Loop through the lines of a text file downloaded from the Internet. 
"""

import sys
import urllib.request

url = "http://oit2.scps.nyu.edu/~meretzkm/python/string/romeo.txt"

try:
    lines = urllib.request.urlopen(url)
except urllib.error.URLError as error:
    print("urllib.error.URLError", error)
    sys.exit(1)

for line in lines:
    s = line.decode("utf-8") #Convert sequence of bytes to string of characters.
    print(s, end = "")       #s already ends with a newline.
    
lines.close()
sys.exit(0)
