import re
import time
from pprint import pprint

from netmiko import ConnectHandler


class Graph:

    def __init__(self):
        self.vertices = list()
        self.edges = {}

    def add_vertex(self, v):
        self.vertices.append(v)
        self.edges[v] = {}

    def add_edge(self, v1, v2, wieght):
        if v1 and v2 in self.vertices:
            self.edges[v1][v2] = wieght
            self.edges[v2][v1] = wieght
            return True
        else:
            return False

    def get_graph(self):
        graph = {}
        for vertex in self.edges.keys():
            graph[vertex] = []
            # print(vertex)
            for edge in self.edges[vertex].items():
                node_id = edge[0]
                weight = edge[1]

                graph[vertex].append((node_id, weight))

            # print(v.id)

        return graph

    def get_edge(self, vertex_id):
        pass


def get_info(host):
    print(f"\nGetting Facts for host {host}")

    pattern_hostname = re.compile("hostname (.*)")
    pattern_ospf_nbr = re.compile("Neighboring Router ID:.(.*)")
    pattern_router_id = re.compile("Advertising Router: (.*)")

    data = {}
    data['host'] = host

    connect_data = {
        'device_type': 'cisco_ios',
        'host': host,
        'username': 'cisco',
        'password': 'cisco',
    }
    connection = ConnectHandler(**connect_data)

    cmd_hostname = connection.send_command("show run | inc hostname")

    data['hostname'] = pattern_hostname.findall(cmd_hostname).pop()

    cmd_ospf_nbrs = connection.send_command("show ip ospf database router self-originate")

    data['router_id'] = pattern_router_id.findall(cmd_ospf_nbrs).pop()
    data['nbrs'] = pattern_ospf_nbr.findall(cmd_ospf_nbrs)
    pprint(data)
    return data


def test_graph():
    G = Graph()

    n1 = "R1"
    n2 = "R2"
    n3 = "R3"
    n4 = "R4"

    G.add_vertex(n1)
    G.add_vertex(n2)
    G.add_vertex(n3)
    G.add_vertex(n4)

    # print(G.vertices)
    G.add_edge(n1, n2, 15)
    G.add_edge(n1, n3, 10)
    G.add_edge(n2, n3, 100)
    G.add_edge(n2, n4, 25)
    # pprint(G.edges)
    graph = G.get_graph()

    pprint(graph)


def main():
    G = Graph()

    hosts = [
        '192.168.1.183',
        '192.168.1.172',
        '192.168.1.191',
        '192.168.1.195',
    ]
    facts = []

    for host in hosts:
        facts.append(get_info(host))

    print("\nPlease Wait, Building Graph Data.\n")
    for fact in facts:
        hostname = fact.get("hostname")
        router_id = fact.get("router_id")

        G.add_vertex(hostname)

        time.sleep(1)

        for f in facts:
            if router_id in f.get("nbrs"):
                e_hostname = f.get("hostname")
                G.add_edge(hostname, e_hostname, 1)

    print("\nResults:")
    print(G.get_graph())


if __name__ == "__main__":
    main()
