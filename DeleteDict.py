d1={1:"Python",2:"C++",3:"C",4:"JAVA",5:"MySql"}
print(d1)
n = int(input("Enter the no of terms you want to delete: "))
print("Enter the values one by one")
while(n!=0):
    ch = int(input())
    del d1[ch]
    n = n-1
print("After Deletion")    
print(d1)    
    
