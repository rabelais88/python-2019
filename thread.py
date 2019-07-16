import threading
import time
import datetime
import random

g_count = 0


def testfunc():
    global g_count
    g_count += 1
    closure_count = g_count
    time.sleep(random.randint(0, 5))
    print("current count", closure_count)


threads = []


def createThread():
    th = threading.Thread(target=testfunc)
    th.start()
    return th


for i in range(5):
    threads.append(createThread())

# caveat
# threads can't be created out of map() function
print(list(threads))
