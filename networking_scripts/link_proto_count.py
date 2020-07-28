from netmiko import ConnectHandler
import re
from rich.console import Console
from rich.table import Table
import threading, queue
import csv
from netmiko import NetmikoAuthenticationException, NetmikoTimeoutException
import argparse

'''
This Script  reads from the specified csv file and executes a log parse function. 

This script utilizes threading and will consistently read the csv file and preform the worker action.


usage: link_proto_count.py [-h] [--parse PARSE]

Cisco Log Parser

optional arguments:
  -h, --help     show this help message and exit
  --parse PARSE  Select the CSV file you would like to open
  
######
Example Results: 
Please Wait, Inspecting: 192.168.1.165
Link flaps detected: 6 - Protocol flaps detected: 8

'''


def get_logs(host):
    table = Table(title="Link/Proto Updown")
    table.add_column("Protocol Flaps", justify="center", style="cyan", no_wrap=True)
    table.add_column("Line Flaps", justify="center", style="cyan", no_wrap=True)

    console = Console()

    cisco1 = {
        "host": host,
        "username": "cisco",
        "password": "cisco",
        "device_type": "cisco_ios",
        "timeout": 10
    }

    console.print(f"\nPlease Wait, Inspecting: {host}", style="red")

    try:
        net_connect = ConnectHandler(**cisco1)
        command_result = net_connect.send_command("show log")
        net_connect.disconnect()

    except NetmikoAuthenticationException:
        console.print(f'Unable to authenticate to {host}')
        return

    except NetmikoTimeoutException:
        console.print(f'Connection Timed-out to host: {host}')
        return

    except Exception:
        raise

    pattern_proto_updown = re.compile("%LINEPROTO-5-UPDOWN")
    pattern_link_updown = re.compile("%LINK-3-UPDOWN")

    matches_proto_updown = pattern_proto_updown.findall(command_result)
    matches_link_updown = pattern_link_updown.findall(command_result)

    console.print(
        f"Link flaps detected: {len(matches_link_updown)} - Protocol flaps detected: {len(matches_proto_updown)}")


q = queue.Queue()


def worker():
    while True:
        host = q.get()

        get_logs(host)
        q.task_done()


threading.Thread(target=worker, daemon=True).start()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Cisco Log Parser")

    parser.add_argument("--parse", help="Select the CSV file you would like to open")

    args = parser.parse_args()
    if args.parse:
        FILE_NAME = args.parse
        while True:
            file = open(FILE_NAME, "r")
            print(f"Opening {FILE_NAME}")
            reader = csv.reader(file)

            for host in reader:
                if host:
                    q.put(host[0])

            q.join()
            file.close()

    parser.print_help()
