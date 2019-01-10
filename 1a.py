import matplotlib.pyplot as plt
import math

def p(d, n):
    x = 1
    y = x*2
    z=d;
    for i in range(n):
        x=x*z/d
        z-=1
    return 1-x


def pa(d, n):
    x = ((-n)*(n-1))/(2*d)
    return 1-math.pow ( math.e , x)

d=365

lista1 = [p(d, i) for i in range(60)]
lista2 = [pa(d, i) for i in range(60)]

plt.plot(range(60), lista1, label="p")
plt.plot(range(60), lista2, label="pa")
plt.show()