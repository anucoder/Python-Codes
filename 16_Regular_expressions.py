import re

######################################
# MATCHING TERMS #####################
######################################

patterns = ['term1','term2']

text = "this is string with term1, not with the other"

for pattern in patterns:
    print("I'm searching for "+pattern)

    if re.search(pattern,text):
        print("Match")
    else:
        print("No match")

match = re.search("term1",text)
print(match.start())


###################################
#   SPLITTING TERMS ###############
###################################


split_term = "@"
email = "user@gmail.com"

print(re.split(split_term,email))


###################################
# FIND ALL INSTANCES OF MATCH ####
###################################

print(re.findall("match","test phrase match , match in middle"))
