#Lists

mylist = ['string',1,2,3,True,[1,2,3]] #nested list with multiple data typles
#print(mylist)

print(len(mylist))
print(mylist[0])
print(mylist[-1])
print(mylist[0:3])
print(mylist[5][2])  #indexing nested list

#Lists are immutable
mylist[0] = 'NEW ITEM'
print(mylist)

#append
mylist.append("appended item")
print(mylist)

listtwo = ['x','y','z']
mylist.append(listtwo)
print(mylist)

mylist.extend(listtwo)
print(mylist)

#removing the last item
item = mylist.pop()
print(mylist)

#remobving using indexing
item = mylist.pop(0)
print(mylist)

#reverse
mylist.reverse()
print(mylist)   #no cpy string required

#sort
mylist.sort()
print(mylist)

#list comprehensions
matrix = [[1,2,3],[4,5,6],[7,8,9]]
firstCol = [row[0] for row in matrix]

print(firstCol)
