from functools import reduce

class DeviceLink:
    def __init__(self, **kwargs):
        self.status = kwargs.get("status", False)
        self.name = kwargs.get("name", None)
        self.id = kwargs.get("id")


def reduce_on(l1: DeviceLink, l2: DeviceLink):
    print(l1, l2)
    if l1.id > l2.id:
        return l1
    else:
        return l2


def main():
    d1 = DeviceLink(status=True, name='l1', id=1)
    d2 = DeviceLink(status=True, name='l2', id=2)
    d3 = DeviceLink(status=False, name='l3', id=3)
    d4 = DeviceLink(status=False, name='l4', id=4)
    links = [d1, d2, d3, d4]

    results = reduce(reduce_on, links)

    print(results.name)




if __name__ == "__main__":
    main()
