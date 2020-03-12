#In pyhton class name is Capitalized

class Dog():
    #class object attribute
    species = "mammal"
    #initialization method
    #self keyword tells that this method refers to itself or belongs to class.
    def __init__(self,breed,name):
        self.breed = breed
        self.name = name


mydog = Dog("lab","Tommy")
print(mydog.breed)
print(mydog.name)
print(mydog.species)
