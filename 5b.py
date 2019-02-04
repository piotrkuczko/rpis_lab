import random

import numpy as np
import datetime
import matplotlib.pyplot as plt
from statistics import median
from statistics import mean
from collections import Counter

input = np.loadtxt('us_births_69_88.csv', skiprows=1, delimiter=',', dtype=int)
inputNotebook = input

def correctDate (day, month):
    isValidDate = True
    try:
        datetime.datetime(int(2020), int(month), int(day))
    except ValueError:
        isValidDate = False
    return isValidDate

# input 0 - month, 1 - day

births = []
maks = 0
for date in input:
	# if correctDate(date[1], date[0]):
	births.append(date[2])
	maks = max(date[2], maks)

input = np.asarray(births)
births = input
births = births * births.size

average = np.average(births)
t = np.zeros((3, input.size))

lower = []
higher = []
cnt = 0
i = 0
for birth in births:
	if birth == average:
		t[0][cnt] = t[1][cnt] = i
		t[2][cnt] = average
		cnt += 1
	elif birth < average:
		lower.append((i, birth))
	else:
		higher.append((i, birth))
	i += 1

while len(lower) > 0 and len(higher) > 0:
	l = lower.pop()
	h = higher.pop()
	
	t[0][cnt] = l[0]
	t[1][cnt] = h[0]
	t[2][cnt] = l[1]
	cnt += 1

	h = (h[0], h[1] - average + l[1])
	if h[1] == average:
		t[0][cnt] = t[1][cnt] = h[0]
		t[2][cnt] = h[1]
		cnt += 1
	elif h[1] < average:
		lower.append(h)
	else:
		higher.append(h)

N = 100000
randomDays = np.random.randint(0, input.size, N)
randomForDays = np.random.randint(0, average, np.size(randomDays))

resultDays = np.where(randomForDays > t[2][randomDays], t[1][randomDays], t[0][randomDays])

c = np.bincount(resultDays.astype(int))
cGood = [i for i in c if i > 10]

sum = np.sum(births)
sumGood = np.sum([i for i in births if i > 100000])

p = births / sum
pGood = [i for i in births if i > 100000]
pGood = pGood / sumGood

f = p * N
fGood = pGood * N

s = 0
for i in range(len(f)):
	s += ((f[i] - c[i]) ** 2) / f[i]

sGood = 0
for i in range(len(fGood)):
	sGood += ((fGood[i] - cGood[i]) ** 2) / fGood[i]

from scipy.stats import chi2, chisquare

print(s, sGood)
print(1 - chi2.cdf(x=s, df=371), 1 - chi2.cdf(x=sGood, df=365))
print(chisquare(c, f))
print(chisquare(cGood, fGood))