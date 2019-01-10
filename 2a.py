import numpy as np
import datetime
import matplotlib.pyplot as plt
import pandas as pd
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


tab = np.loadtxt('dane.txt', skiprows=1, delimiter=',', dtype=int)
maksimum = 0
for i in range (len(tab)):
    if (correctDate(tab[i][1], tab[i][0]) == False):
        tab[i][2] = 0
    else:
        maksimum = max(maksimum, tab[i][2])

print(maksimum)
#y = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

def losujDzien ():
    zbiór = set()
    i=0
    while True:
        dzien = random.randint(1, len(tab)-1)
        kt = random.randint(1, maksimum)
        if (kt <= tab[dzien][2]):
            if dzien in zbiór:
                return i
            else:
                zbiór.add(dzien)
            i+=1
    return i

lista3 = [losujDzien() for i in range(100000)]
print ("Median: " + str(median(lista3)))
print ("Average: " + str(mean(lista3)))


lista3.sort()
labels, values = zip(*Counter(lista3).items())

indexes = np.arange(len(labels))
width = 1

plt.bar(indexes, values, width)
plt.xticks(indexes + width * 0.5, labels)
plt.show()

