
import numpy as np
import datetime
import matplotlib.pyplot as plt
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
tablist = list()
maksimum = 0
for i in range (len(tab)):
    if (correctDate(tab[i][1], tab[i][0]) == False):
        tab[i][2] = 0
    else:
        maksimum = max(maksimum, tab[i][2])
        tablist.append (tab[i][2])
tab2 = np.asarray(tablist)
print(tab2)
print(maksimum)
#y = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]


ileDni = 10000
ilelos = ileDni*100

ls = np.random.randint(1, maksimum, ilelos)
dni = np.random.randint(1, 366, ilelos)
X = tab2[dni]
Y = dni[X > ls]

print (Y)



def losujDni (ile):
    wyniki = list()
    zbiór = set()
    i=0
    kt = 0
    while ile > 0:
        dzien = Y[kt]
        kt+=1
        if dzien in zbiór:
            wyniki.append(i)
            ile -= 1
            zbiór.clear()
            i = 0
        else:
            zbiór.add(dzien)
            i += 1
    return wyniki


lista3 = losujDni(ileDni)

print ("Median: " + str(median(lista3)))
print ("Average: " + str(mean(lista3)))


lista3.sort()
labels, values = zip(*Counter(lista3).items())

indexes = np.arange(len(labels))
width = 1

plt.bar(indexes, values, width)
plt.xticks(indexes + width * 0.5, labels)
plt.show()

