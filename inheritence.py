class Person:
    def __init__(self, name=None, roll=None):
        self.name = name
        self.roll = roll

class Child(Person):
    def __init__(self, name=None, roll=0):
        super().__init__(name, roll)
        self.roll+=1

p1 = Child("Anushka", 727)
print(p1.name)
print(p1.roll)

p2 = Child("sneha")
print(p2.name)
print(p2.roll)