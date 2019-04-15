"""
设在主线程中启动子线程A

A.join()  --> 表示主线程等待直到子线程A退出，无论是正常退出还是异常退出
A.join(2) --> 表示主线程等待子线程2秒后继续往下执行

若有多个子线程均设置了等待时间，则总等待时间为所有等待时间之和。如：
A.join(1)
B.join(2)
C.join(3)
主线程等待时间为6秒

若子线程为守护线程，主线程退出后，子线程直接强制退出

"""


import threading, time


def sub_thread(msg):
    print("{} enter at {}.".format(msg, time.time()))
    time.sleep(2)
    print("{} exit at {}.".format(msg, time.time()))


if __name__ == "__main__":
    print("main thread enter at {}".format(time.time()))
    t = []
    for i in [1,2,3]:
        t.append(threading.Thread(target=sub_thread, args=("thread_"+str(i),)))

    t[0].start()
    t[1].start()
    t[2].start()

    t[0].join(1)
    print("thread_1 join end")
    t[1].join(2)
    print("thread_2 join end")
    t[2].join(3)
    print("thread_3 join end")

    print("main thread exit at {}".format(time.time()))

    