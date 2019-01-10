import numpy as np
import datetime
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import random
from statistics import median
from statistics import mean
from collections import Counter

def correctDate (day, month):
    isValidDate = True
    try:
        datetime.datetime(int(2020), int(month), int(day))
    except ValueError:
        isValidDate = False
    return isValidDate

arr = []
for i in range(0, 13):
    arr.append([])

tab = np.loadtxt('dane.txt', skiprows=1, delimiter=',', dtype=int)
a = np.random.random((31, 12))
for i in range (len(tab)):
    if (correctDate(tab[i][1], tab[i][0])):
        a[tab[i][1]-1][tab[i][0]-1] = tab[i][2]

y = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

data = pd.DataFrame(a, columns=y, index = range(1, 32, 1))
ax = sns.heatmap(data.T)

for item in ax.get_yticklabels():
    item.set_rotation(45)

plt.show()

listaPom = []
suma = 0
listaPom.append(tab[i][2])
for i in range (1, len(tab)):
    listaPom.append(tab[i][2]+listaPom[i-1])
    suma = listaPom[i]

def losujDzien ():
    zbiór = set()
    i=0
    while True:
        liczba = random.randint(1, suma)
        index = np.searchsorted(listaPom, liczba)
        if index in zbiór:
            return i
        else:
            zbiór.add(index)
        i+=1
    return i

lista3 = [losujDzien() for i in range(10000)]
print ("Median: " + str(median(lista3)))
print ("Average: " + str(mean(lista3)))


lista3.sort()
labels, values = zip(*Counter(lista3).items())

indexes = np.arange(len(labels))
width = 1

plt.bar(indexes, values, width)
plt.xticks(indexes + width * 0.5, labels)
plt.show()

