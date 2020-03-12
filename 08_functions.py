def my_func(param='default'):
    """
    This is a docstring
    """
    rstr = "my first python function {}".format(param)
    print(type(rstr))   #returns the type of rstr
    return rstr

print(my_func())

#filter
mylists = [1,2,3,4,5,6,7,8]

def even_bool(num):
    return num%2 == 0  #returns true if even_bool

evens = filter(even_bool,mylists)
print(list(evens))

#Lambda expression
#replacing function even_bool with lambda expression
evens2 = filter(lambda num:num%2==0,mylists)
print(list(evens2))

#in keyword
print('x' in [1,2,3,'x'])
