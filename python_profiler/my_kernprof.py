
import sys
import numpy as np

@profile
def bbb():
  sum = 0
  for i in range(10000):
    sum += i ** 2
  print(sum)

@profile
def aaa():
  print(np.sum([i ** 2 for i in range(10000)]))

bbb()
aaa()