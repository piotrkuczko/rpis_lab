import random

import numpy as np
import datetime
import matplotlib.pyplot as plt
from statistics import median
from statistics import mean
from collections import Counter

def distr (k):
    if k == 0.0:
        return 1/2
    return 1.0/(4.0*abs(k)*(abs(k)+1.0))

prec = 1
lista = []
lista3 = []
for i in np.arange(-10.0, 10.0, prec):
    lista3.append(distr(i))
    lista.append(i)
plt.plot(lista, lista3)
plt.ylim(0.0,1.0)
plt.xlim(-10,10)
plt.show()


losowe = np.random.random(200000)
kt = 0

def randomWithDistrubation(k):
    global kt
    global losowe
    y = losowe[kt]
    kt+=1
    if y < 0.5:
        return 0
    znak = -1 if (0.5 < y) and (y < 0.75) else 1
    x = losowe[kt]
    kt+=1
    wyn = np.ceil(1 / (x)) - 1
    return znak * wyn

zdystrybuanta = [randomWithDistrubation(i) for i in range(10000)]
pref = []

suma = 0
for i in range(10000):
    suma += zdystrybuanta[i]
    pref.append(suma/(i+1))
plt.plot(pref)
plt.show()

czesciowy = []
mediana = []
for i in range(1000):
    czesciowy.append(zdystrybuanta[i])
    mediana.append(median(czesciowy))
plt.plot(mediana)
plt.show()

zwektorozywanaDystr = np.vectorize(randomWithDistrubation)

samplowanie = np.fromfunction(zwektorozywanaDystr, (10000,))

plt.hist(samplowanie, bins=range(-10, 10))
plt.show()
