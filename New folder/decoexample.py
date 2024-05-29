import threading   
import time

def disp1():
    for x in range(10):
        print('thread1 is running')
        time.sleep(2)
        
def disp2():
    for x in range(10):
        print('thread2 is running')
        time.sleep(2)

t1=threading.Thread(target=disp1)
print(t1)
t2=threading.Thread(target=disp2)
print(t2)
t1.start()
t1.join()
t2.start()


