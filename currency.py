#a cashier has currency notes of denomination 1,5,10 write of currency notes or each amount to be withdrawn from the user and print the total number of currecce notes of eachdenomation he cashier have given
price=int(input("enter price of withdrawn:"))
r10=price//10
price=price%10
r5=price//5
price=price%5
r1=price//1
print("10 rupes notes is:",r10,end="\n")
print("5 rupes notes is:",r5)
print("1 rupes notes is:",r1)