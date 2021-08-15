from collections import defaultdict
from dataclasses import dataclass
from enum import Enum


class ConnectionStratigies(Enum):
    SSH = 'SSH'
    TELNET = 'TELNET'
    SNMP = 'SNMP'
    NETCONF = 'NETCONFG'
    RESTCONF = 'RESTCONF'


class Strategy:
    @staticmethod
    def handle_strategy(*args, **kwargs):
        raise NotImplemented


class SSHCiscoStrategy(Strategy):
    @staticmethod
    def handle_strategy(*args, **kwargs):
        device = kwargs.get('device')
        _vendor = 'cisco'
        if _validate_vendor(device, _vendor):
            print(f"Connnecting to: {device.ipv4_addr}, Vendor: {_vendor}")


class SSHJuniperStrategy(Strategy):
    @staticmethod
    def handle_strategy(*args, **kwargs):
        device = kwargs.get('device')
        _vendor = 'juniper'
        if _validate_vendor(device, _vendor):
            print(f"Connnecting to: {device.ipv4_addr}, Vendor: {_vendor}")




@dataclass
class Device:
    ipv4_addr: str
    vendor: str


def _validate_vendor(device: Device, vendor):
    if device.vendor == vendor:
        return True
    else:
        return False


class ConnectionHandler:

    def __init__(self):
        self._strategies = defaultdict(Strategy)


    def connect(self, device: Device, strategy: str):
        _strategy = strategy_map.get(ConnectionStratigies(strategy).value)
        _strategy.handle_strategy(device=device)


if __name__ == "__main__":
    strategy_map = defaultdict(set)
    strategy_map = {
        'SSH': {
            SSHJuniperStrategy,
            SSHCiscoStrategy
        }

    }

    connection_handler = ConnectionHandler()

    r1 = Device(ipv4_addr='1.1.1.1', vendor='cisco')
    r2 = Device(ipv4_addr='1.1.1.1', vendor='juniper')

    connection_handler.connect(device=r1, strategy='SSH')
    connection_handler.connect(device=r2, strategy='SSH')
