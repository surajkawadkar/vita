import math
a=int(input("enter x^2 term"))
b= int(input("enter bx term"))
c=int(input("neter conmstant term"))
print("expression is",a,'x^2'+'+',b,'x +',c)
nume=(b*b-4*a*c)
den= (2*a)
print(nume)
print(den)


r1=-b+(math.sqrt(nume/den))
r2=-b-((math.sqrt(nume/den)))
print(r1)
print(r2)

