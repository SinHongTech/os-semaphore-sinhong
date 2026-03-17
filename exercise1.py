from threading import Thread, Semaphore
import time
import random

# Shared buffer
buffer = []

# Semaphores
mutex = Semaphore(1)      # mutual exclusion
empty = Semaphore(100)    # empty slots
full = Semaphore(0)       # filled slots


# Producer function
def producer(pid):
    while True:
        # Produce a pair
        p1 = f"P{pid}-A"
        p2 = f"P{pid}-B"

        # Wait for 2 empty slots
        empty.acquire()
        empty.acquire()

        # Critical section
        mutex.acquire()
        buffer.append(p1)
        buffer.append(p2)
        print(f"Producer {pid} produced: {p1}, {p2} | Buffer size: {len(buffer)}")
        mutex.release()

        # Signal 2 full slots
        full.release()
        full.release()

        time.sleep(random.uniform(0.1, 0.5))


# Consumer function
def consumer():
    while True:
        # Wait for 2 full slots
        full.acquire()
        full.acquire()

        # Critical section
        mutex.acquire()
        p1 = buffer.pop(0)
        p2 = buffer.pop(0)
        print(f"Consumer packaged: {p1}, {p2} | Buffer size: {len(buffer)}")
        mutex.release()

        # Signal 2 empty slots
        empty.release()
        empty.release()

        time.sleep(random.uniform(2, 4))


# Create threads
producers = [Thread(target=producer, args=(i,)) for i in range(3)]
cons = Thread(target=consumer)

# Start threads
producers[0].start()
producers[1].start()
cons.start()