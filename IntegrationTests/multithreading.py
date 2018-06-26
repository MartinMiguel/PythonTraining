#https://pymotw.com/2/threading/
#The simplest way to use a Thread is to instantiate it with a target function
#and call start() to let it begin working.

import threading

def worker():
    """thread worker function"""
    print ('Worker')
    return

threads = []
for i in range(3):
    t = threading.Thread(target=worker)
    threads.append(t)
    t.start()
###########
def worker(num):
    """thread worker function"""
    print ('Worker: %s' % num)
    return

threads = []
for i in range(3):
    t = threading.Thread(target=worker, args=(i,))
    threads.append(t)
    t.start()
###########
#Determining the Current Thread
import logging
from datetime import datetime
import time

logging.basicConfig(level=logging.DEBUG,
                    format='[%(levelname)s] (%(threadName)-10s) %(message)s',
                    )

def worker():
    print("Starting worker: " + datetime.now().strftime("%H:%M:%S.%f"))
    logging.debug('Starting')
    time.sleep(2)
    logging.debug('Exiting')
    print("Ending worker: " + datetime.now().strftime("%H:%M:%S.%f"))

def my_service():
    print("Starting my_service: " + datetime.now().strftime("%H:%M:%S.%f"))
    logging.debug('Starting')
    time.sleep(4)
    logging.debug('Exiting')
    print("Ending my_service: " + datetime.now().strftime("%H:%M:%S.%f"))

t = threading.Thread(name='my_serviceX', target=my_service)
w = threading.Thread(name='workerX', target=worker)
w2 = threading.Thread(target=worker) # use default name

w.start()
w2.start()
t.start()
################
#Un daemon, servicio o programa residente es un tipo especial de proceso informático no interactivo,
#es decir, que se ejecuta en segundo plano
