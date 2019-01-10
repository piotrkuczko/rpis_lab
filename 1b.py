import matplotlib.pyplot as plt
import random
import numpy as np
from collections import Counter
from statistics import median
from statistics import mean

def emp(d):
    zbiór = set()
    i = 1
    while True:
        liczba = random.randint(1, d)
        if liczba in zbiór:
            return i
        else:
            zbiór.add(liczba)
        i+=1
    return i

d=365

lista3 = [emp(d) for i in range(10000)]
print ("Median: " + str(median(lista3)))
print ("Average: " + str(mean(lista3)))


lista3.sort()
labels, values = zip(*Counter(lista3).items())

indexes = np.arange(len(labels))
width = 1

plt.bar(indexes, values, width)
plt.xticks(indexes + width * 0.5, labels)
plt.show()