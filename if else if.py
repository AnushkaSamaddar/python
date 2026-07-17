#Write a program to check whether a given year is a leap year
# n=int(input("enter a year: "))
# if n%400==0 or n%4==0 and n%100!=0:
#     print("the given year ",n,"is a leap year")
# else:
#     print("the given year ",n,"is not a leap year")
#Write a program to check whether a number is a palindrome.
n=int(input("enter a no: "))
num=n
reverse=0
while(n>0):
    lst=n%10
    reverse=reverse *10 + lst 
    n=n//10

if reverse==num:
    print("the number is palindrome")
else:
    print("thr no is not palindrome")     