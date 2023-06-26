num=int(input("enter number"))
no=num
s=0
while(num>0):
    d=num%10
    s=s*10+d
    num=num//10
if s==no:
    print("no is palindrome")
else:
    print("not palindrome")