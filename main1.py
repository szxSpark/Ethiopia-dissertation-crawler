from website1 import crawler as crawler1
from website2 import crawler as crawler2
from website3 import crawler as crawler3
from website4 import crawler as crawler4
import threading
import time

'''
website13 不一样
'''

exitFlag = 0


class myThread(threading.Thread):  # 继承父类threading.Thread
    def __init__(self, name, crawler):
        threading.Thread.__init__(self)
        self.name = name
        self.crawler = crawler

    def run(self):  # 把要执行的代码写到run函数里面 线程在创建后会直接运行run函数
        news_list = self.crawler()
        for i, news in enumerate(news_list):
            filename = "./news/"+self.name+"_"+str(i)+".txt"
            print(self.name, ": writing", filename, news)
            with open(filename, "w", encoding="utf-8")as f:
                f.write(str(news))


# 创建新线程
thread1 = myThread("Thread-1", crawler1)
thread2 = myThread("Thread-2", crawler2)
thread3 = myThread("Thread-3", crawler3)
thread4 = myThread("Thread-4", crawler4)

# 开启线程
thread1.start()
thread2.start()
thread3.start()
thread4.start()


