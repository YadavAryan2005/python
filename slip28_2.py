l1=[]
l2=[]

n=int(input("Enter limit of first limit :"))
for i in range(0,n):
    l1.append(int(input("Enter number to add 1st list")))
n1=int(input("Enter limit of second limit :"))
for i in range(0,n1):
    l2.append(int(input("Enter number to add 1st list")))
t1=list(zip(l1,l2))
print(t1)