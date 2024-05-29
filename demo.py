class errorp (Exception):
   pass
class accept(errorp):
   try:
       n=int(input("enter no"))
       if(n>0):
           raise errorp("negetiveno")
       else:
           print("corrct no")
   except errorp as e:
       print(e)