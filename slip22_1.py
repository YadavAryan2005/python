class String:
    def __init__(self):
        self.s1=input("enter your string")
    def __mul__(self,n):
        for i in range(0,n):
            print(self.s1)
ob=String()
ob*5