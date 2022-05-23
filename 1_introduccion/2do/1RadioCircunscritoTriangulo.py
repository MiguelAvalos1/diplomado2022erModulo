import math

print("\n\n Radio de un circulo inscrito en un triángulo dados sus lados a, b, y c.  \n")

a=float(input("Inserte valor de a: "))
b=float(input("Inserte valor de b: "))
c=float(input("Inserte valor de c: "))

suma=a+b

if (c < suma):
    s=0.5*(a+b+c)
    r=math.sqrt(s*(s-a)*(s-b)*(s-c))/s
    r_rounded = round(r, 2)
    print("R=",r_rounded)
else:
    print("El valor de c no puede ser mayor a la suma de a y b")