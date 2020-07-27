from netmiko import ConnectHandler
from getpass import getpass
import csv

hosts = []

results = []
for host in hosts:
    cisco1 = {
        "host": host,
        "username": "pyclass",
        "password": getpass(),
        "device_type": "cisco_ios",
    }

    net_connect = ConnectHandler(**cisco1)

    results.append(net_connect.send_command("show ip route"))
