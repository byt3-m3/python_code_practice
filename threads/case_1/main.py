from threading import Thread
from queue import Queue
import time

_q13 = Queue()
_q12 = Queue()

'''
This script demonstrates the use of Threads and Queues in Python. 

It will Launch 3 Threads, each of which will preform a distinct actions 

Worker 3 will create the NodeClass object and pass it to Worker 1 for processing

Worker 1 will obtain the node_type of the device and send it to Worker 2 for final computation 

worker 2 will take the contents of the object and save it to a file and erase the memory buffer


'''

def worker_1():
    while True:
        time.sleep(.5)
        item = _q13.get()
        print(f"\nWorker 1 Got Worker 3 item: {item.hostname}")
        print(f"\nWorker 1 Getting node_type for {item.hostname}")
        item.node_type = "cisco_ios"
        print(f'\nWorker 1 view of Que13 Size is: {len(_q13.queue)}')
        print(f"\nWorker 1 adding {item.hostname} for Worker 2")
        time.sleep(2)
        _q12.put(item)


def worker_2():
    while True:
        time.sleep(3)
        item = _q12.get()
        print(f'\nWorker 2 view of Que12 Size is: {len(_q12.queue)}')
        print(f"\nWorker 2 Got Worker 1 item: {item.hostname}")
        with open("results.txt", "a+") as f:
            if isinstance(item.mgmt_ip, tuple):
                item.mgmt_ip = item.mgmt_ip[0]

            f.write(f'hostname: {item.hostname}; mgmt_ip: {item.mgmt_ip}; node_type: {item.node_type} \n')

        del item


def worker_3():
    class NodeClass:
        def __init__(self, hostname, mgmt_ip, node_type):
            self.hostname = hostname
            self.mgmt_ip = mgmt_ip,
            self.node_type = node_type

    for i in range(30):
        n = NodeClass(hostname=f'R{i + 1}', mgmt_ip=str(f'10.99.0.{i +1}'), node_type=None)
        print(f"\nWorker 3 adding {n.hostname} for Worker 1")
        time.sleep(1)
        _q13.put(n)


def main():
    t1 = Thread(target=worker_1)
    t2 = Thread(target=worker_2)
    t3 = Thread(target=worker_3)

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()


if __name__ == "__main__":
    main()
