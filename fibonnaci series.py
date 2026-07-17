#fibonnaci series
n=int(input("enter a numbber: "))
a=0
b=1
print(a,b ,end=" ")
for i in range(n):
    sum=a+b
    print(sum, end=" ")
    a=b
    b=sum
