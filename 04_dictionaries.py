my_stuff = {"key1" : "value1", "key2" : "value2"}
print(my_stuff["key2"])
print(my_stuff)   #maintains no order

#multiple datatype with nested dictionaries and lists
my_dict = {"key1" : 123, "key2" : "value2", "key3" : {'123' : [1,2,"grabme"]}}
print(my_dict["key3"]['123'][2])  #accessing grabme
print((my_dict["key3"]['123'][2]).upper())

#reassigning dictionaries
my_diet = {'bfast' : "milk" , "lunch" : "oats"}
my_diet['lunch'] = 'pizza'
print(my_diet)

#appending
my_diet["dinner"] = "salad"
print(my_diet)
