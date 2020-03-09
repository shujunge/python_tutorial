##python性能分析

### line_profiler
* line_profiler
* kernprof
上面的工具主要是可以统计每行代码的执行次数和执行时间等，时间单位为微妙。
### timeit
```python
import timeit
def fun():
  for i in range(100000):
    a = i * i
timeit.timeit('fun()', 'from __main__ import fun', number=1)
```

### profile
```python

import profile

def fun():
   for i in range(100000):
      a = i * i
profile.run('fun()')

```

### cProfile
```python
import cProfile

def fun():
   for i in range(100000):
      a = i * i
cProfile.run('fun()')
```

### memory_profiler

```sysbase

pip install memory_profiler  
pip install psutil  
```
使用：
```
1.在需要测试的函数加上@profile装饰
2.执行命令： python -m memory_profiler yourcode.py 
```
### [内存泄漏检测](https://blog.csdn.net/xiarendeniao/article/details/7872619)

* python使用引用计数和垃圾回收来释放（free）Python对象
* 引用计数的优点是原理简单、将消耗均摊到运行时；缺点是无法处理循环引用
* Python垃圾回收用于处理循环引用，但是无法处理循环引用中的对象定义了__del__的情况，而且每次回收会造成一定的卡顿
* gc module是python垃圾回收机制的接口模块，可以通过该module启停垃圾回收、调整回收触发的阈值、设置调试选项
* 如果没有禁用垃圾回收，那么Python中的内存泄露有两种情况：要么是对象被生命周期更长的对象所引用，比如global作用域对象；要么是循环引用中存在__del__
* 使用gc module、objgraph可以定位内存泄露，定位之后，解决很简单
* 垃圾回收比较耗时，因此在对性能和内存比较敏感的场景也是无法接受的，如果能解除循环引用，就可以禁用垃圾回收。
* 使用gc module的DEBUG选项可以很方便的定位循环引用，解除循环引用的办法要么是手动解除，要么是使用weakref

在Python中，一切都是对象，又分为mutable和immutable对象。
二者区分的标准在于是否可以原地修改，“原地“”可以理解为相同的地址。
可以通过id()查看一个对象的“地址”，如果通过变量修改对象的值，但id没发生变化，那么就是mutable，否则就是immutable．
```python
a=5
id(a)
a=6
id(a)
```
为了避免频繁的申请、释放内存，避免大量使用的小对象的构造析构，python有一套自己的内存管理机制。
在巨著《Python源码剖析》中有详细介绍，在python源码obmalloc.h中也有详细的描述．

### [graphviz](https://blog.csdn.net/lanchunhui/article/details/51488375)

命令
```sysbase
dot test.dot -Tpng -o test.png
dot test.dot -Tpdf -o test.pdf
```
### [gprof2dot](https://zhuanlan.zhihu.com/p/24495603)
```sysbase
gprof2dot -f pstats mkm_run.prof | dot -Tpng -o mkm_run.png

```
### vprof 可视化性能到网页

```
vprof -c c yourcode.py 
默认网址localhost:8000
```
