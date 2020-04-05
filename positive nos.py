n = int(input("Enter the number of elements: "))
mylist = []
print("Enter the values:-")
for i in range(0,n):
    a=int(input())
    mylist.append(a)
for i in mylist:
    if(i>0):
        print(str(i),end=" ")
