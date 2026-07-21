n=int(input("enter the no of lines: "))
for i in range(n):
    for j in range(i+1):
        print(j+1,end=" ")
    print()  
#Print a right triangle star pattern of height n.
for i in range(n):
    for j in range(i+1):
        print("*",end=" ")
    print() 
#Print an inverted star triangle       
for i in range(n):
    for s in range(n):
        print(end=" ")
    for j in range(n-i):
        print("*",end=" ")
    print()    
for i in range(n):
    for j in range(1,i):
        print("*",end=" ")
    print()    
