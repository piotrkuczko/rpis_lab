import random

import numpy as np
import datetime
import matplotlib.pyplot as plt
from statistics import median
from statistics import mean
from collections import Counter

N = 1000
lamb = 10
lista = []
lista2 = []
for i in range(N):
    lista.append(np.random.poisson(10))

for i in range(N):
    suma = 0
    for j in range(i+1):
        suma += lista[j]
    suma /= (i+1)
    lista2.append(suma)



lista2.sort();
labels, values = zip(*Counter(lista2).items())

indexes = np.arange(len(labels))
width = 1

plt.bar(indexes, values, width)
plt.xticks(indexes + width * 0.5, labels)
plt.show()

print(lista)
print(lista2)