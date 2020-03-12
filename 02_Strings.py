
mystring = 'Hello world'
print(mystring)

#indexing
print(mystring[0])

#negative indexing
print(mystring[-1])

#slicing
print(mystring[2:]) #strat at index 2 and print all the way to end
print(mystring[:3]) #strat at index 0 atill the index 2 (not including 3)
print(mystring[2:5]) #strat at index 2 and till 4
print(mystring[:]) #sentire mystring
print(mystring[::2]) #step size of 2

#immutable
#mystring[0] = 'x'

#Basic methods
x = mystring.upper()  #uppercase
y = mystring.lower()  #lowercase
z = mystring.capitalize() #capitalize first letter

print(x)
print(y)
print(z)

spl =  mystring.split('o') #returns an array of strings after splitting
print(spl)

#print formatting

#inserting strings
x = "Item One : {} ,Item Two : {}".format("dog","cat")
print(x)

x = "Item One : {y} ,Item Two : {x}".format(x="dog",y="cat")
print(x)
