# B) Create a class circles having members radius. Use operator overloading to add the
# radius of two circle objects. Also display the area of circle
class circles:
    def __init__(self):
        self.n=int(input("enter radius"))
    def __add__(self,ob):
        rad=ob.n+self.n
        print("area of circle",3.14*rad*rad)
ob=circles()
ob1=circles()
ob+ob1

