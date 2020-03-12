def get_num():
    import random
    digits = list(range(10))
    random.shuffle(digits)
    #print(digits[:3])
    numstr = ""
    numgen = numstr.join(map(str,digits[:3]))
    print(numgen)
    return numgen

def len_not_correct(num):
    if(len(guess)>3 or len(guess)<3):
        return True

def is_match(num1,num2):
    if(num1[0]==num2[0] or num1[1]==num2[1] or num1[2]==num2[2]):
        return True

def is_close(num1,num2):
    if(num2[0] in list(num1) or num2[1] in list(num1) or num2[2] in list(num1)):
        return True

numreq = get_num()
while True:
    guess = str(input("What is your guess? "))
    #print(guess)
    if(len_not_correct(guess)):
        print("Please enter a 3 digit number")
    elif(guess==numreq):
        print("Number guessed correclty")
        break
    elif(is_match(numreq,guess)):
        print("MATCH !! Try Again !")
    elif(is_close(numreq,guess)):
        print("CLOSE !! Try Again !")
    else:
        print("WROMG ANSWER! :(")
