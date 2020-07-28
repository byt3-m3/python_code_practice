from rich.table import Table
from rich.console import Console
from netmiko import ConnectHandler

def main():
    hosts = ["192.168.1.165", "192.168.1.2"]
    console = Console()
    main_results = []
    for host in hosts:

        result_dict = {}
        cisco1 = {
            "host": host,
            "username": "cisco",
            "password": "cisco",
            "device_type": "cisco_ios",
        }

        console.print(f"\nPlease Wait, Connecting to: {host}", style="red")
        net_connect = ConnectHandler(**cisco1)
        command_result = net_connect.send_command("show ip route")

        pattern = compile('O.*(\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}).*via.(\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})..*, (.*)')

        regex_results = pattern.findall(command_result)
        if len(regex_results) > 0:
            table = Table(title="OSPF Routes")
            table.add_column("Subnet", justify="center", style="cyan", no_wrap=True)
            table.add_column("next_hop", justify="center", style="cyan", no_wrap=True)
            table.add_column("interface", justify="center", style="cyan", no_wrap=True)

            for r in regex_results:
                table.add_row(f"{r[0]}", f"{r[1]}", f"{r[2]}")

                main_results.append(result_dict)

            console.print(table, style="red")

        if len(regex_results) > 0:
            print("No OSPF routes detected.")
            console.print(table, style="red")


if __name__ == "__main__":
    main()
