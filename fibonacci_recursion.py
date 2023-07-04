#print fibonacci series using recursion of nth term
def fibonacci(a,b,n):
    if(n==0):
        return
    else:
        print(a)
        c=a+b
        a=b
        b=c
        fibonacci(a,b,n-1)

a=0
b=1
n=int(input("enter limit of fibonacci series:")) 
fibonacci(a,b,n)     
