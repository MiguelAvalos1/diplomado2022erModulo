#   2-x
## e - 7x=0
#resolver usando 1 metodo y graficar
#Metodo usado Newton

from math import exp

def f(x):# Función
    return exp(2-x)-7*x

def f2(x):# Derivada: 
    return -exp(2-x)-7

x0=1.5
x1=x0-f(x0)/f2(x0)
x2=x1-f(x1)/f2(x1)
x3=x2-f(x2)/f2(x2)

print('La raiz es ',x3)