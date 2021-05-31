def wallis(n):
    pi = 0.0   
    for i in range(1, n):
        x = 4 * (i ** 2)
        y = x - 1
        z = float(x) / float(y)
        if (i == 1):
            pi = z
        else:
            pi *= z
    pi *= 2
    return pi
n=input()
print(wallis(n))

import random
import math
def monte_carlo(total):
 inside = 0
 for i in range(0, total):
  x = random.random()
  y = random.random()
  if math.sqrt(x**2 + y**2) < 1.0:
    inside += 1
 pi = (float(inside) / total) * 4
 return pi
total=input()
print(monte_carlo(total))
