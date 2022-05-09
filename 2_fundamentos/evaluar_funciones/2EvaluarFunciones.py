import math
from cmath import sin

print("\n\n Evaluar las funciones y=sin(2x) para x=1.3\n En la función y=e^(1-2x) en x=-0.45 \n")

print("\n\nFunción y=sin(2x) para x=1.3")

x=1.3

y = sin(2*x)
print("Resultado 1: ",y)


print("\n\nFunción y=e^(1-2x) en x=-0.45 ")

x=-0.45
y2 = math.exp(1-2*(x))
print("Resultado 2: ",y2)