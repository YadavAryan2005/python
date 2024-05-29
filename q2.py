from datetime import date,datetime
class InvalidDate(Exception):
    pass
class date1:
    def __init__(self,y,m,d):
        self.y=y
        self.m=m
        self.d=d
    def check(self):
        try:
          if self.m < 1 or self.m > 12:
                raise InvalidDate("Invalid month")
          if self.m == 2:
                if (self.y % 4 == 0 and self.d > 29) or (self.y % 4 != 0 and self.d > 28):
                    raise InvalidDate("Invalid date")
          elif self.m in {4, 6, 9, 11} and self.d > 30:
                raise InvalidDate("Invalid date")
          elif self.d > 31:
                raise InvalidDate("Invalid date")
          da=date(self.y,self.m,self.d)
          print("Date =",da)
        except InvalidDate as e:
            print(e)
y=int(input("Enter year :"))
m=int(input("Enter month :"))
d=int(input("Enter day :"))
ob=date1(y,m,d)
ob.check()