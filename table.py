#accept number from user and display table of that number
num=int(input("enter number:"))
for i in range(1,11):
    print(num*i,end="\t")