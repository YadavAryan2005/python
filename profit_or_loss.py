#accept selling and cost price from user find how many profit or loss 
sel=int(input("enter selling price:"))
cost=int(input("enter cost price:"))
if(sel>cost):
    print("profit=",sel-cost)
else:
    print("loss=",cost-sel)
