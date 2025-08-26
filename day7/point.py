class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return f"({self.x}, {self.y})"
    def __add__(self, p):
        return Point(self.x + p.x, self.y + p.y)
    def __sub__(self, p):
        return Point(self.x - p.x, self.y - p.y)
    def __mul__(self, n):
        return Point(self.x * n, self.y * n)
    def __truediv__(self, n):
        return Point(self.x / n, self.y / n)
    def __floordiv__(self, n):
        return Point(self.x // n, self.y // n)
    def __mod__(self, n):
        return Point(self.x % n, self.y % n)
    def __pow__(self, n):
        v1=1
        v2=1
        for i in range(n):
            v1 *= self.x
            v2 *= self.y
        return Point(v1, v2)
    def __lt__(self, p):
        if(self.x < p.x and self.y < p.y):
            return True
        else:
            return False
    def __eq__(self, p):
        if(self.x == p.x and self.y == p.y):
            return True
        else:
            return False
    def __gt__(self, p):
        if(self.x > p.x and self.y > p.y):
            return True
        else:
            return False
    def __le__(self, p):
        if(self.x <= p.x and self.y <= p.y):
            return True
        else:
            return False
    def __ge__(self, p):
        if(self.x >= p.x and self.y >= p.y):
            return True
        else:
            return False
    def __ne__(self, p):
        if(self.x != p.x and self.y != p.y):
            return True
        else:
            return False
a=Point(41, 50)
b=Point(2, 3)
print(f"The first object is: {a}")
print(f"The second object is: {b}")
print(f"The sum of {a} and {b} is {a+b}")
print(f"The difference of {a} and {b} is {a-b}")
print(f"The product of {a} and 5 is {a*5}")
print(f"The division of {a} and 5 is {a/5}")
print(f"The integer division of {a} and 5 is {a//5}")
print(f"The modulus of {a} and 5 is {a%5}")
print(f"The power of {b} is {b**3}")
print(f"{a} == {b} is {a==b}")
print(f"{a} >= {b} is {a>=b}")
print(f"{a} <= {b} is {a<=b}")
print(f"{a} > {b} is {a>b}")
print(f"{a} < {b} is {a<b}")
print(f"{a} != {b} is {a!=b}")