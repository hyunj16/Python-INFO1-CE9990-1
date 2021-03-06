"""
findmonth3.py

Search a list with the index function.
"""

import sys

try:
    month = input("Please type a month, e.g., January: ")
except EOFError:
    sys.exit(1)

months = [
    None,        # 0 dummy value to give January index 1
    "January",   # 1
    "February",  # 2
    "March",     # 3
    "April",     # 4
    "May",       # 5
    "June",      # 6
    "July",      # 7
    "August",    # 8
    "September", # 9
    "October",   #10
    "November",  #11
    "December"   #12
]

try:
    i = months.index(month)
except ValueError:
    print("Bad month \"", month, "\".", sep = "")
    sys.exit(1)

print("Thank you, ", month, " is month number ", i, ".", sep = "")
sys.exit(0)
