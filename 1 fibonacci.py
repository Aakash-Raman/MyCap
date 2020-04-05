t1 = 0
t2 = 1
n = int(input("Enter the no of terms: "))
i=0
while(i<n):
    print(str(t1),end=" ")
    nextterm = t1+t2
    t1 = t2
    t2 = nextterm
    i += 1
    
