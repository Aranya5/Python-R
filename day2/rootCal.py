a = int(input("Enter value of a:"))
b = int(input("Enter value of b:"))
c = int(input("Enter value of c:"))

D = b*b- 4*a*c
if D < 0:
    print("No real roots")
    rootReal = (-b / (2*a))
    rootImg = ((-D)**0.5 / (2*a))
    print("Roots are:", rootReal, "+", rootImg, "i and", rootReal, "-", rootImg, "i")
elif D == 0:
    root = -b / (2*a)
    print("One real root:", root)
else:
    root1 = (-b + D**0.5) / (2*a)
    root2 = (-b - D**0.5) / (2*a)
    print("Roots are:", root1, "and", root2)