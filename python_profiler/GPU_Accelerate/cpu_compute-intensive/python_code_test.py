import math
import numpy as np
a=range(1,50000000)

def f(x):
    return 3*math.log(x)+math.cos(x)**2
from time import time
start=time()
r=[f(t) for t in a]
print("math time:",time()-start)  ##23.7s

start=time()
a=np.array(a)
r=3*np.log(a)+np.cos(a)**2
print("numpy time:",time()-start) ##12.5s


from numba import jit
@jit
def sum(a):
	return 3*np.log(a)+np.cos(a)**2
start=time()
sum(a)
print("numba time:",time()-start) ##3.5s

import numexpr as ne
ne.set_num_threads(1)
f='3*log(a)+cos(a)**2'
start=time()
r=ne.evaluate(f)
print("numexpr1 time:",time()-start) ##1s


import numexpr as ne
ne.set_num_threads(2)
f='3*log(a)+cos(a)**2'
start=time()
r=ne.evaluate(f)
print("numexpr2 time:",time()-start)##0.54s

