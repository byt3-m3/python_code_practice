class Device:
    def __init__(self, hostname):
        self.name = hostname


class DeviceList:
    def __init__(self):
        self.items = []

    def __iter__(self):
        return self

    def __next__(self):
        return self.items

    def add_device(self, d: Device):
        self.items.append(d)


def main():
    device_list = DeviceList()
    d1 = Device(hostname="d1")
    d2 = Device(hostname="d2")
    d3 = Device(hostname="d3")

    device_list.add_device(d1)
    device_list.add_device(d2)
    device_list.add_device(d3)

    for i in device_list:
        print(i)


if __name__ == "__main__":
    main()
