# liczymy sobie średnią i przerzucamy kubki do średniej, potem losujemy dzień i mamy dwa dni do wyboru
import random

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
for i in range (len(tab)):
    if (correctDate(tab[i][1], tab[i][0]) == True):
        tablist.append (tab[i][2])

input = (np.asarray(tablist)) * len(tablist)
srednia = (int)(np.average(input))
#print (srednia/len(tablist))

#przelewanie kubelkow
wyniki = np.zeros((3, input.size))
nis = list()
wys = list()
k = 0

for i in range(input.size):
    if input[i] == srednia:
        wyniki[0][k] = wyniki[2][k] = (int)(i)
        wyniki[1][k] = (int)(srednia)
        k += 1
    elif input[i] > srednia:
        wys.append((i, input[i]))
    else:
        nis.append((i, input[i]))

while len(nis) > 0 and len(wys) > 0:
    n = nis.pop()
    w = wys.pop()
    wyniki[0][k]=(int)(n[0])
    wyniki[1][k] = (int)(n[1])
    wyniki[2][k] = (int)(w[0])
    k += 1
    w = (w[0], (w[1]-srednia+n[1]))
    if w[1] == srednia:
        wyniki[0][k] = wyniki[2][k] = (int)(w[0])
        wyniki[1][k] = (int)(srednia)
        k += 1
    elif w[1] > srednia:
        wys.append(w)
    else:
        nis.append(w)

# for i in range (k):
#     print (wyniki[0][i], wyniki[1][i], wyniki[2][i])

#zwektoryzowane losowanie
ileDni = 100000
ilelos = ileDni*100

wysokosc = np.random.randint(0, srednia, ilelos)
dni = np.random.randint(0, input.size, ilelos)
randomDays = np.where (wysokosc > wyniki[1][dni], wyniki[2][dni], wyniki[0][dni])

#print (randomDays)

#losuje pierwsze wystapienie dnia
def losujDni (ile):
    wynikiprv = list()
    zbiór = set()
    kt = 0
    while ile > 0:
        dzien = randomDays[kt]
        kt+=1
        if dzien in zbiór:
            wynikiprv.append(len(zbiór)+1)
            ile -= 1
            zbiór.clear()
        else:
            zbiór.add(dzien)
    return wynikiprv

#print(wyniki.size/3)
resultPlt = losujDni(ileDni)

print ("Median: " + str(median(resultPlt)))
print ("Average: " + str(mean(resultPlt)))


resultPlt.sort()
labels, values = zip(*Counter(resultPlt).items())

indexes = np.arange(len(labels))
width = 1

plt.bar(indexes, values, width)
plt.xticks(indexes + width * 0.5, labels)
plt.show()
