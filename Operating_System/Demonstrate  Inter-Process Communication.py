import time
from multiprocessing import Process, Value

def writer(shared_value):
    for i in range(1, 6):
        shared_value.value = i
        print("Writer wrote:", i)
        time.sleep(1)

def reader(shared_value):
    for i in range(1, 6):
        time.sleep(1)
        print("Reader read:", shared_value.value)

if __name__ == "__main__":
    # Create shared memory variable
    shared_value = Value('i', 0)

    # Create processes
    p1 = Process(target=writer, args=(shared_value,))
    p2 = Process(target=reader, args=(shared_value,))

    # Start processes
    p1.start()
    p2.start()

    # Wait for processes to finish
    p1.join()
    p2.join()

    print("Process communication completed.")
