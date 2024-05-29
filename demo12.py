# Write a Python class to find the validity of a string of parentheses, '(', ')',
# '{' , '}', '[' , ']'. These brackets must be closed in the correct order for
# example "( )" and "( ) [ ] { }" are valid but "[ )", "({[)]" and "{{{" are
# invalid
e=input("enter your expression")
k=0
for i in range(0,len(e)-1,2):
    if(e[i]=='{' and e[i+1]!='}'):
        k=1
        break
    if(e[i]=='(' and e[i+1]!=')'):
        k=1
        break
    if(e[i]=='[' and e[i+1]!=']'):
        k=1
        break
if(k==1):
    print("invalid")
else:
    print("valid")
    




