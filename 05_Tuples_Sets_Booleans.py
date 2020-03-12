#tuples are immutable sequesnces
#Sets are unordered collections of unique elements
# Booleans - True & False & 0 &1

#tuple
t = (1,2,3,True,'string')
#t[0] = 'NEW'  ---> gives error as tuples are immutable
#every thing lese is as similar to lists

#Sets-- unordered collections
x = set()

x.add(1)
x.add(2)
x.add(3)
x.add(3)

print(x)  #adds unique elements

converted = set([1,1,1,2,3,3,3,4,5,5,5,4,4])
print(converted)
