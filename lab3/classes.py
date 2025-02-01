#1
class Text:
    def __init__(self):
        self.c=""
    def getString(self):
        self.c="ivab"
    def printString(self):
        print(self.c.upper())
t=Text()
t.getString()
t.printString()

#2
class Shape:
    def __init__(s):
        pass 
    def area(s):
        return 0  
class Square(Shape):
    def __init__(s, length):
        s.length = length
    def area(s):
        return s.length ** 2 
a = Shape()
print(a.area())  
b = Square(4)
print(b.area())  

#3
class Shape:
    def __init__(s):
        pass 
    def area(s):
        return 0 
class Square(Shape):
    def __init__(s, length):
        s.length = length
    def area(s):
        return s.length ** 2 
class Rectangle(Shape):
    def __init__(s, length, width):
        s.length = length
        s.width = width
    def area(s):
        return s.length * s.width 
a = Shape()
print(a.area()) 
b = Square(4)
print(b.area())  
c = Rectangle(4, 6)
print(c.area()) 


#4
import math
class point():
    def __init__(self,x1,y1,x2,y2 ):
        self.x1=x1
        self.y1=y1
        self.x2=x2
        self.y2=y2
    def show(self):
        print(f"Coordinats: [{self.x1}, {self.y1}], [{self.x2},{self.y2}]")
    def move(self,a,b,c,d):
        self.x1=a
        self.y1=b
        self.x2=c
        self.y2=d
    def dist(self):
        c=(self.x1-self.x2)**2 + (self.y1 - self.y2)**2
        t=math.sqrt(c)
        return t
print("enter the coordinates: ")
a,b,c,d=map(int, input(). split())
t=point(a,b,c,d)
t.show()
print("Distance: ", t.dist())
e,f,g,h=map(int, input(). split())
t.move(e,f,g,h)
t.show()
print("Distance: ", t.dist())


#5
class account():
    def __init__(self, owner, balance):
        self.owner=owner
        self.balance=balance
    def cur(self):
        print(f"Username: {self.owner}")
        print(f"Current balance: {self.balance}")
    def deposit(self, mon):
        self.balance += mon
        print(f"Deposited:{mon} tg.New balance: {self.balance}")
    def withdraw(self, mon):
        if mon<=self.balance:
            self.balance-=mon
            print(f"Withdrew:{mon} tg.New balance: {self.balance}")
        else:
            print("Not enough money.")
a=input()
b=int(input())           
t=account(a,b)
t.cur()
print("Insert:")
s=int(input())
t.deposit(s)
print("Output:")
d=int(input())
t.withdraw(d)


#6
print("How many elements:")
b=int(input())
c=[]
for i in range(2,b+1):
    a=int(input())
    c.append(a)
p = lambda n: n > 1 and all(n % i != 0 for i in range(2, int(n ** 0.5) + 1))
primes = list(filter(p, c))
print(primes)  