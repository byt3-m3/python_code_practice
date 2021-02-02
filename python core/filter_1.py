from random import choice


class Device:
    def __init__(self, **kwargs):
        self.vendor = kwargs.get("vendor", False)
        self.hostname = kwargs.get("hostname", None)
        self.id = kwargs.get("id")


def create_devices(count=10):
    vendors = ['cisco', 'juniper']

    devices = []
    for i in range(count):
        devices.append(Device(vendor=choice(vendors), hostname='r1', id=(i + 1)))
    return devices


# Anonmoyous functions
filter_cisco = lambda x: x.vendor == "cisco"
filter_juniper = lambda x: x.vendor == "juniper"


# filter functions
def filter_cisco_func(device: Device):
    if device.vendor == 'cisco':
        return True
    else:
        return False


def filter_juniper_func(device: Device):
    if device.vendor == 'juniper':
        return True
    else:
        return False


def lambda_example(devices: list):
    print("\nLambda Example")
    cisco_nodes = list(filter(filter_cisco, devices))

    juniper_nodes = list(filter(filter_juniper, devices))

    print(f'Cisco Nodes: {len(cisco_nodes)}')
    print(f'Juniper Nodes: {len(juniper_nodes)}')

    print(len(cisco_nodes) + len(juniper_nodes))


def function_example(devices: list):
    print("\nFunction Example")

    cisco_nodes = list(filter(filter_cisco_func, devices))

    juniper_nodes = list(filter(filter_juniper_func, devices))

    print(f'Cisco Nodes: {len(cisco_nodes)}')
    print(f'Juniper Nodes: {len(juniper_nodes)}')

    print(len(cisco_nodes) + len(juniper_nodes))

def main():

    devices = create_devices(500)
    function_example(devices)

    devices = create_devices(500)
    lambda_example(devices)



if __name__ == "__main__":
    main()
