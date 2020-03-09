"""
Python给我们提供了很多接口方便我们能够灵活的进行性能分析，其中主要包含两个类cProfile模块的Profile类和pstat模块的Stats类。
我们可以通过这两个类来将代码分析的功能进行封装以便在项目的其他地方能够灵活重复的使用进行分析。
这里还是需要对Profile以及Stats的几个常用接口进行简单总结：

Profile类:
enable(): 开始收集性能分析数据
disable(): 停止收集性能分析数据
create_stats(): 停止收集分析数据，并为已收集的数据创建stats对象
print_stats(): 创建stats对象并打印分析结果
dump_stats(filename): 把当前性能分析的结果写入文件(二进制格式)
runcall(func, *args, **kwargs): 收集被调用函数func的性能分析数据

Stats类
pstats模块提供的Stats类可以帮助我们读取和操作stats文件（二进制格式）

"""

# import cProfile
# import re
# cProfile.run('re.compile("foo|bar")')
#
# from cProfile import Profile
#
# def runRe():
#     import re
#     re.compile("aaa|bbb")
#
# prof = Profile()
# prof.enable()
# runRe()
# prof.create_stats()
# prof.print_stats()


### liner_profiler

import line_profiler
import sys
import numpy as np

def bbb():
    sum=0
    for i in range(10000):
        sum+=i**2
    print(sum)

profile = line_profiler.LineProfiler(bbb)  # 把函数传递到性能分析器
profile.enable()  # 开始分析
bbb()
profile.disable()  # 停止分析
profile.print_stats(sys.stdout)  # 打印出性能分析结果


def aaa():
  
  print(np.sum([i**2 for i in range(10000)]))

profile = line_profiler.LineProfiler(aaa)  # 把函数传递到性能分析器
profile.enable()  # 开始分析
aaa()
profile.disable()  # 停止分析
profile.print_stats(sys.stdout)  # 打印出性能分析结果

