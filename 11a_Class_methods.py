class Circle():

    pi = 3.14
    #radius=1 is a default parameter
    def __init__(self,radius=1):
        self.radius = radius

    def area(self):
        return self.radius * self.radius * Circle.pi

    def set_radius(self,new_r):
        self.radius = new_r


c = Circle(3)
print(c.radius)
c.radius = 100
#c.set_radius(100)
print(c.radius)
print(c.area())
c.set_radius(500)
print(c.area())
