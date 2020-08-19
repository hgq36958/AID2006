"""
练习：
1.启动2个分子线程，1个线程打印A-Z，26个字母，另外一个线程打印1-52 这52个数字
要求：打印顺序12A34B56C……5152Z
提示：一个线程里也可以有多个锁
"""
from threading import *

# e = Event()
# def fun1():
#     for x in range(65, 91):
#         e.wait(2)
#         print(chr(x))
#         #e.wait(2)
# def fun2():
#     for i in range(1,53):
#         print(i)
#         e.wait(1)
#
# t2 = Thread(target=fun1)
# t1 =Thread(target=fun2)
# t2.start()
# t1.start()
# #fun2()
#
# t2.join()
# t1.join()

lock1=Lock()
lock2=Lock()

def fun1():
    for i in range(1,53,2):
        lock1.acquire()
        print(i)
        print(i+1)
        lock2.release()

def fun2():
    for x in range(65,91):
        lock2.acquire()
        print(chr(x))
        lock1.release()

t1=Thread(target=fun1)
t2=Thread(target=fun2)
lock2.acquire()

t1.start()
t2.start()

t1.join()
t2.join()

