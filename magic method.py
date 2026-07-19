# class Student:
#     def __init__(self,m1,m2):
#         self.m1=m1 
#         self.m2=m2
#     def shownumber(self):
#         print(self.m1,self.m2)
#     def __add__(self,other):
#         newm1=self.m1+other.m1
#         newm2=self.m2+other.m2
#         s3=Student(newm1,newm2)
#         return s3
# obj=Student(53,68)
# obj.shownumber()
# obj2=Student(56,93)
# obj2.shownumber()
# obj3=obj+obj2
# obj3.shownumber()
#opperator overloading
class Complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img
    def shownumber(self):
        print(f"{self.real}i+{self.img}j")
    def __add__(self,other):
        newreal=self.real+other.real
        newimg=self.img+other.img
        return Complex(newreal,newimg)
a=Complex(5,6)
a.shownumber()
b=Complex(2,4)
b.shownumber()
c=a+b
c.shownumber()
#handling polymorphism with class

class Circle:
    def area(self):
        print("Area=pi x r x r")

class Square:
    def area(self):
        print("Area=side x side")

def show_area(shape):
    shape.area()

#Creating object
c=Circle()
s=Square()
show_area(c)
show_area(s)
class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def __gt__(self,other):
        if(self.marks>other.marks):
            return self.marks
        else:
            return other.marks
        
n1=Student("abc",8)
n2=Student("xyz",70)

result=n1.marks>n2.marks
if result==True:
    print("Greater marks: ",n1.name)
else:
    print("Greater marks: ",n2.name)