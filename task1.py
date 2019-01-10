import numpy as np
import random, math
import matplotlib.pyplot as plot


def odl(a, b):
    return a * a + b * b

W = 10
P = W*W*4

def inside(p):
    global W
    a, b = p
    return odl(a, b) <= W

def get_f(a, b):
    return np.random.random() * (b-a) + a;

def get_point():
    global W
    return (get_f(-W, W), get_f(-W, W))

N = 1000000

area = []
inn = 0
for i in range(N):
    inn += inside(get_point())
    area += [P * inn / (i+1) /  W]

plot.ylim([3.06,3.26])
plot.plot(range(0, N), area)
#plot.plot
plot.show()

my_area = area[N-1]
print(my_area)