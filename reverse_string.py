#input string from user and reverse the string
s1=input("enter name:")
j=len(s1)-1
for i in range(0,len(s1)):
    print(s1[j],end="")
    j=j-1
    