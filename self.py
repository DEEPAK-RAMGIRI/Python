class Person:
    def __init__(self,name,value):
        self.name =name
        self.phno =value
    def printing(self):
        print(self.name)
        print(self.phno)
obj1 = Person("name",12345678)
obj1.printing()