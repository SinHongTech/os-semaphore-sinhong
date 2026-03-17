from threading import Thread, Semaphore
import time
import random

a = Semaphore(1)
b = Semaphore(0)
c = Semaphore(0)

# Process Function
def process1():
    while True:
        a.acquire()
        print("H", end="")
        print("E", end="")
        b.release()
        b.release()
def process2():
    while True:
        b.acquire()
        print("L", end="")
        c.release()
def process3():
    while True:
        c.acquire()
        c.acquire()
        print("O", end="")

# Create threads
t1 = Thread(target=process1)
t2 = Thread(target=process2)
t3 = Thread(target=process3)
# Start threads
t1.start()
t2.start()
t3.start()