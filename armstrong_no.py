#check number is palindrome or not
num=int(input("enter number"))
n1=num
s=0
while(num>0):
    d=num%10
    s=s+d*d*d
    num=num//10
if n1==s:
    print("armstrong number")
else:
    print("not armstrong number")