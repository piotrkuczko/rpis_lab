import numpy as np
import random, math
import matplotlib.pyplot as plot


def get_f(a, b):
    return np.random.random() * (b-a) + a;

def f(x):
    if x < -1 or x > 1: x = 1
    return 2 * pow(1 - x*x, 0.5)


# WAY1 :
N = 1000000

x = []
y = []

pole = 0
seg = 1. /N * 2.

val = -1
while val < 1:
    val += seg
    pole += (f(val) + f(val + seg)) / 2 * seg
    x += [val]
    y += [f(val)]

plot.plot(x, y)
plot.show()

print("REAL PI: {}".format(math.pi))

print("WAY1 PI: {}".format(pole))

# WAY 2:

result = 0
for i in range(N):
    result += f(get_f(-1, 1))

result = result / N * 2
print("WAY2 PI: {}".format(result))