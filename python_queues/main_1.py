from queue import SimpleQueue, Queue
import requests
import threading
import time

class Action:
    def __init__(self, id):
        self.id = id

    def __call__(self, *args, **kwargs):
        self.action = requests.get("http://udev.bits.local:5004/v1/nodes")
        return self.action


my_queue = Queue()

for i in range(10):
    a = Action(i + 1)
    my_queue.put(a, block=False, timeout=1)


def worker():
    while True:
        a = my_queue.get(timeout=1)
        print(a.id)
        print(a())

        print("Worker A")
        my_queue.task_done()


def worker_b():
    while True:
        a = my_queue.get(timeout=1)
        print(a.id)
        print(a())

        print("Worker B")
        my_queue.task_done()


def main():
    threading.Thread(target=worker, daemon=True).start()
    threading.Thread(target=worker_b, daemon=True).start()
    my_queue.join()
    print("All Task Complete")


if __name__ == "__main__":
    main()
