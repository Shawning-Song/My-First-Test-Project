import threading, time, os

class MyThread(threading.Thread):
    """
    """

    def run(self):
        global num
        time.sleep(1)

        if lk.acquire(True):
            num += 1
            print("name:{} TID:{} set num to {}".format(self.name, \
                threading.get_ident(), num))
            lk.release()
        print("name:{} exit.".format(self.name))


class MyThreadNoLock(threading.Thread):
    """
    """

    def run(self):
        global num
        time.sleep(1)

        num+=1
        print("name:{} TID:{} set num to {}".format(self.name, \
                threading.get_ident(), num))
        print("name:{} num:{} exit.".format(self.name, num))


num = 0
lk = threading.Lock()

# 这里的锁其实完全没有必要，因为CPython中GIL的限制，同一时刻只可能存在
# 一个python线程运行，并不会有数据访问冲突的场景
if __name__ == "__main__":
    for i in range(10):
        t = MyThreadNoLock()
        t.start()

    time.sleep(3)
    print("final num ", num)
    print("main thread exit.")
