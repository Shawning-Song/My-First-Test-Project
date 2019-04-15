from multiprocessing.pool import Pool
import os, time, random


def worker(msg):
    t_start = time.time()
    print("%s 开始执行，父进程号为%d, 进程号为%d"%(msg, os.getppid(), os.getpid()))
    time.sleep(random.random()*2)
    t_stop = time.time()
    print("%s 执行完毕，耗时%0.2f"%(msg, t_stop-t_start))
    return msg

def callback(result):
    print("结果为{} 进程号为{}".format(result, os.getpid()))

if __name__ == "__main__":
    # 定义一个进程池，最大进程数3
    p_pool = Pool(3) 

    for i in range(10):
        p_pool.apply_async(worker, (i,), callback=callback)

    print("----start----")
    print("主进程号为%d"%os.getpid())
    p_pool.close()
    p_pool.join()
    print("----end----")
