import rpyc


class ServiceAClient:
    def __init__(self, host="localhost", port=8001):
        self.c = rpyc.connect(host, port)

    def run(self):
        return self.c.root.run()

    def add(self, x, y):
        return self.c.root.add(x, y)


if __name__ == "__main__":
    c = ServiceAClient()
    print(c.add(2, 3))
    print(c.run())
