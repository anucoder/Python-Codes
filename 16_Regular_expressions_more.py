import re

str = "RRU-101(D1)"

#Search for a sequence that starts with "he", followed by two (any) characters, and an "o":

x = re.findall(r"^RRU-\w+", str)
print(x)
