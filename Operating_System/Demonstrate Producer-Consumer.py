from multiprocessing import Process, Array, Semaphore
import time

buffer = Array('i', 1)       # Shared memory
empty = Semaphore(1)
full = Semaphore(0)
mutex = Semaphore(1)

def producer():
    for i in range(1, 6):
        empty.acquire()
        mutex.acquire()	

        buffer[0] = i
        print("Produced:", i)

        mutex.release()
        full.release()
        time.sleep(1)

def consumer():
    for i in range(1, 6):
        full.acquire()
        mutex.acquire()

        print("Consumed:", buffer[0])
        buffer[0] = 0

        mutex.release()
        empty.release()
        time.sleep(1)

if __name__ == "__main__":
    p = Process(target=producer)
    c = Process(target=consumer)

    p.start()
    c.start()

    p.join()
    c.join()

    print("Completed")