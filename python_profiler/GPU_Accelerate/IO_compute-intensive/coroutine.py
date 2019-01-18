# import multiprocessing
# import time
# import threading
# # 定义全局变量Queue
# g_queue = multiprocessing.Queue()
#
# def init_queue():
#     print("init g_queue start")
#     while not g_queue.empty():
#         g_queue.get()
#     for _index in range(10):
#         g_queue.put(_index)
#     print("init g_queue end")
#     return
#
#
# # 定义一个IO密集型任务：利用time.sleep()
# def task_io(task_id):
#     print("IOTask[%s] start" % task_id)
#     while not g_queue.empty():
#         time.sleep(3)
#         try:
#             data = g_queue.get(block=True, timeout=1)
#             # print("IOTask[%s] get data: %s" % (task_id, data))
#         except Exception as excep:
#             pass
#             # print("IOTask[%s] error: %s" % (task_id, str(excep)))
#     # print("IOTask[%s] end" % task_id)
#     return
#
# g_search_list = list(range(10000))
# # 定义一个计算密集型任务：利用一些复杂加减乘除、列表查找等
# def task_cpu(task_id):
#     print("CPUTask[%s] start" % task_id)
#     while not g_queue.empty():
#         count = 0
#         for i in range(1000000):
#             count += pow(3*2, 3*2) if i in g_search_list else 0
#         try:
#             data = g_queue.get(block=True, timeout=1)
#             # print("CPUTask[%s] get data: %s" % (task_id, data))
#         except Exception as excep:
#             pass
#             # print("CPUTask[%s] error: %s" % (task_id, str(excep)))
#     # print("CPUTask[%s] end" % task_id)
#     return task_id
#
# if __name__ == '__main__':
#     print("cpu count:", multiprocessing.cpu_count(), "\n")
#
#     print("========== 直接执行IO密集型任务 ==========")
#     init_queue()
#     time_0 = time.time()
#     task_io(0)
#     print("结束：", time.time() - time_0, "\n")
#
#     print("========== 多线程执行IO密集型任务 ==========")
#     init_queue()
#     time_0 = time.time()
#     thread_list = [threading.Thread(target=task_io, args=(i,)) for i in range(5)]
#     for t in thread_list:
#         t.start()
#     for t in thread_list:
#         if t.is_alive():
#             t.join()
#     print("结束：", time.time() - time_0, "\n")
#
#     print("========== 多进程执行IO密集型任务 ==========")
#     init_queue()
#     time_0 = time.time()
#     process_list = [multiprocessing.Process(target=task_io, args=(i,)) for i in range(multiprocessing.cpu_count())]
#     for p in process_list:
#         p.start()
#     for p in process_list:
#         if p.is_alive():
#             p.join()
#     print("结束：", time.time() - time_0, "\n")
#
#     print("========== 直接执行CPU密集型任务 ==========")
#     init_queue()
#     time_0 = time.time()
#     task_cpu(0)
#     print("结束：", time.time() - time_0, "\n")
#
#     print("========== 多线程执行CPU密集型任务 ==========")
#     init_queue()
#     time_0 = time.time()
#     thread_list = [threading.Thread(target=task_cpu, args=(i,)) for i in range(5)]
#     for t in thread_list:
#         t.start()
#     for t in thread_list:
#         if t.is_alive():
#             t.join()
#     print("结束：", time.time() - time_0, "\n")
#
#     print("========== 多进程执行cpu密集型任务 ==========")
#     init_queue()
#     time_0 = time.time()
#     process_list = [multiprocessing.Process(target=task_cpu, args=(i,)) for i in range(multiprocessing.cpu_count())]
#     for p in process_list:
#         p.start()
#     for p in process_list:
#         if p.is_alive():
#             p.join()
#     print("结束：", time.time() - time_0, "\n")
#
#


# import requests
# import time
#
# def consumer():
#     r = ''
#     while True:
#         n = yield r
#         if not n:
#             return
#         # print('[CONSUMER] Consuming %s...' % n)
#         r = requests.get(n).status_code
#
#
# def produce(c):
#     c.send(None)
#     for i in range(73000, 73100):
#         request_url = "http://www.jb51.net/article/%d.htm" % i
#         # print('[PRODUCER] Producing %s...' % request_url)
#         r = c.send(request_url)
#         # print('[PRODUCER] Consumer return: %s' % r)
#     c.close()
#
#
# async_start = time.time()
# produce(consumer())
# print("async_start:",time.time() - async_start)
#
# sync_start = time.time()
# for i in range(73000, 73100):
#     url = "http://www.jb51.net/article/%d.htm" % i
#     response = requests.get(url)
# print("sync_start:",time.time() - sync_start)

import asyncio
import threading

async def hello(index):  # 通过关键字async定义协程
  print('Hello world! index=%s, thread=%s' % (index, threading.currentThread()))
  await asyncio.sleep(1)  # 模拟IO任务
  print('Hello again! index=%s, thread=%s' % (index, threading.currentThread()))

from time import time
start=time()
loop = asyncio.get_event_loop()  # 得到一个事件循环模型
tasks = [hello(10000), hello(20000)]  # 初始化任务列表
loop.run_until_complete(asyncio.wait(tasks))  # 执行任务
loop.close()
print("time: ",time()-start)
