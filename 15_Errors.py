#errors and exceptions
try:
    f = open('Simpel.txt','r')  #read permissions
    f.write("Test write to simple.txt")  #trying to write
except IOError:
    print("COULD NOT FIND THE FILE OR READ DATA")
except:
    print("Oops ! Unknown error")
else:
    print("SUCCESS")
    f.close()
print("Hello world") #continue with the program execution


################################################
#              finally                       #
##############################################

try:
    f = open('Simple.txt','w')  #read permissions
    f.write("Test write to simple.txt")  #trying to write
except IOError:
    print("COULD NOT FIND THE FILE OR READ DATA")
finally:
    print("I will always work no matter what") #continue with the program execution
