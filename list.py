l=list(input("enter a list: "))
element=input("enter the element: ")
for i in range(0,len(l)):
    if(element==l[i]):
        print(element,"present in",i,"index")
        break
    else:
        print(element,"not found")
#write a program to find the frequency of each element in the list
l=list(input("enter a list: "))
l1=[]
l2=[]
for i in range(len(l)):
    if l[i] not in l1:
     count=1
     for j in range(i+1,len(l)):
        if l[i]==l[j]:
            count+=1
     print(l[i],"frequency",count)
     l1.append(l[i]) 
     if count==1:
        l2.append(l[i])
print(l1)
print(l2)


