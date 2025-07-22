a = int(input("Enter value of a:"))
b = int(input("Enter value of b:"))
c = int(input("Enter value of c:"))

root1 = (-b + (b**2 -4*a*c)**0.5) / (2*a)
root2 = (-b - (b**2 -4*a*c)**0.5) / (2*a)
print("Roots are:", root1, "and", root2)