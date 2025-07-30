def gcd(n,m):
  min = n
  if(m>n):
    min = n
  else:
    min = m
  for i in range(1, min+1, 1):
    if(n % i == 0 and m % i == 0):
      gcd = i
  return gcd

a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
print("GCD of", a, "and", b, "is", gcd(a, b))