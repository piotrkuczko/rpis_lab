# liczymy sobie średnią i przerzucamy kubki do średniej, potem losujemy dzień i mamy dwa dni do wyboru
import random

import numpy as np
import datetime
import matplotlib.pyplot as plt
from statistics import median
from statistics import mean
from collections import Counter

from scipy import stats


def correctDate (day, month):
    isValidDate = True
    try:
        datetime.datetime(int(2020), int(month), int(day))
    except ValueError:
        isValidDate = False
    return isValidDate


tab = np.loadtxt('dane.txt', skiprows=1, delimiter=',', dtype=int)
tablist_correctDate = list()
tablist_unCorrectDate = list()
for i in range (len(tab)):
    if (correctDate(tab[i][1], tab[i][0]) == True):
        tablist_correctDate.append (tab[i][2])
    tablist_unCorrectDate.append(tab[i][2])

input_correctDate = (np.asarray(tablist_correctDate)) * len(tablist_correctDate)
input_unCorrectDate = (np.asarray(tablist_unCorrectDate)) * len(tablist_unCorrectDate)


#print (srednia/len(tablist_correctDate))

#przelewanie kubelkow


def input_to_random_days (input):
    srednia = (int)(np.average(input))
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
    ileDni = 100000
    ilelos = ileDni * 100
    wysokosc = np.random.randint(0, srednia, ilelos)
    dni = np.random.randint(0, input.size, ilelos)
    randomDays = np.where(wysokosc > wyniki[1][dni], wyniki[2][dni], wyniki[0][dni])
    return randomDays
        

# for i in range (k):
#     print (wyniki[0][i], wyniki[1][i], wyniki[2][i])

#zwektoryzowane losowanie
randomDaysCorrect = input_to_random_days(input_correctDate)
randomDaysUncorrect = input_to_random_days(input_unCorrectDate)

#-----------------------------------------------------------------------------------------------

def wyznaczS (input, randomDays):
    N = 10000
    p = []
    f = []
    sum = 0
    for i in input:
        sum += int(i)
    for i in input:
        p.append(i / sum)
    for i in p:
        f.append(i*N)
    days = []
    d = int(max(randomDays))
    print (d)
    for i in range(d+1):
        days.append(0)
    for i in range(N):
        days[int(randomDays[i])] += 1
    S = 0
    for i in range(len(f)):
        S += ((f[i] - days[i]) ** 2) / f[i]
    return S

S_correct = wyznaczS(input_correctDate, randomDaysCorrect)
S_uncorrect = wyznaczS(input_unCorrectDate, randomDaysUncorrect)
print(S_correct)
print (S_uncorrect)

print(1-stats.chi2.cdf(S_correct, len(input_correctDate)-1))
print(1-stats.chi2.cdf(S_uncorrect, len(input_unCorrectDate)-1))
