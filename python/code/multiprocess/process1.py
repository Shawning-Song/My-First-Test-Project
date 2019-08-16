import os
from multiprocessing import Process
import time


def process_func(name:str):
    print("subprocess running....")
    while True:
        print("subprocess<{}> pid:{} ppid: {}".format(name, os.getpid(), os.getppid()))
        time.sleep(1)
  
if __name__ == "__main__":
    # 打印主进程PID
    print("main process PID: ", os.getpid())

    # 创建进程对象
    p = Process(target=process_func, args=("test1",))

    # 启动进程
    p.start()

    # 主进程睡眠
    time.sleep(5)

    # 结束子进程
    p.terminate()
    p.join()

    print("main process exit.")