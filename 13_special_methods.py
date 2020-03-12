class Book():

    def __init__(self,Title,author,pages):
        self.Title = Title
        self.author = author
        self.pages = pages

    def __str__(self):
        return "Title :{}, Author :{}, pages :{}".format(self.Title,self.author,self.pages)

    def __len__(self):
        return self.pages

    def __del__(self):
        print("A book is destroyed")


mybook = Book("Edges of Dreams", "Anagha", 200)
print(mybook)
print(len(mybook))
del mybook
