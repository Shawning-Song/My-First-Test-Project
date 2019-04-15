"""
主线程和子线程之间的关系
1. 默认情况下，子线程不是守护线程，主线程退出后，子线程继续执行直到退出
2. 子线程可以通过setDaemon接口设置为守护线程，主线程退出后，子线程被强制结束
"""

import threading, time

def sub_thread(msg):
    print("{} enter at {}.".format(msg, time.time()))
    time.sleep(3)
    print("{} exit at {}.".format(msg, time.time()))


if __name__ == "__main__":
    print("main thread enter at {}".format(time.time()))

    # create undaemon thread
    t1 = threading.Thread(target=sub_thread, args=("unDaemon",))
    t1.start()

    # create daemon thread
    t2 = threading.Thread(target=sub_thread, args=("Daemon",))
    t2.setDaemon(True)
    t2.start()

    time.sleep(1)
    print("main thread exit at {}.".format(time.time()))
