from threading import *

import time

s=Semaphore(3)

def wish(name,age):
    for i in range(3):
        s.acquire()
        print('hi',end='')
        time.sleep(1)
        print(name,age)
        s.release()
t1=Thread(target=wish,args=('teju',16))
t2=Thread(target=wish,args=('prince',17))
t3=Thread(target=wish,args=('darshani',18))
t4=Thread(target=wish,args=('mohini',20))
t1.start()
t2.start()
t3.start()
t4.start()
