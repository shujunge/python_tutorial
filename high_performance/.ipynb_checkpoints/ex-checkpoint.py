# import unittest

# @profile
# def some_fn(nbr):
# 	return nbr * 2

# some_fn(4)

"""
# 内存测试
python -m memory_profiler ex.py
# 可视化
mprof run memory_profiler_test.py 
mprof plot 
mprof clean

# cpu性能测试
kernprof -l -v ex.py
"""

import unittest

"""
添加一个 no-op 修饰器(你可以在完成性能分析之后移
除 它 )。 如 果 在 名 字 空 间 中 寻 找 不 到 @profile 修 饰 器 ( 因 为 没 有 使 用
line_profiler 或者 memory_profiler),那么我们写的 no-op 版本的修饰器
就会被加入名字空间。如果 line_profiler 或者 memory_profiler 已经将新
的函数加入名字空间,那么我们 no-op 版本的修饰器就会被忽略
"""
# # line_profiler
# if 'builtins' not in dir() or not hasattr(builtins, 'profile'):
#     import builtins
#     def profile(func):
#         def inner(*args, **kwargs):
#             return func(*args, **kwargs)
#         return inner
#     builtins.__dict__['profile'] = profile


# memory_profiler
if 'builtins' not in dir() or not hasattr(builtins, 'profile'):
    import builtins
    def profile(func):
        def inner(*args, **kwargs):
            return func(*args, **kwargs)
        return inner
    builtins.__dict__['profile'] = profile

@profile
def some_fn(nbr):
	return nbr * 2

class TestCase(unittest.TestCase):
	def test(self):
		result = some_fn(2)
		self.assertEquals(result, 4)
"""
kernprof -v -l ex.py
python -m memory_profiler ex.py
"""
