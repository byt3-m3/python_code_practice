import rpyc
from rpyc.utils.server import ThreadedServer

import logging

logging.basicConfig(level=logging.DEBUG)


class ServiceA(rpyc.Service):

    def exposed_run(self):
        print(self)
        return True

    def exposed_add(self, x, y):
        return x + y


if __name__ == "__main__":
    t = ThreadedServer(ServiceA, port=8001)
    print("Server Started")
    t.start()
