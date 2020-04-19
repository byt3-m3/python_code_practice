import re
import time
from pprint import pprint

import matplotlib.pyplot as plt
import networkx as nx
from netmiko import ConnectHandler


class Vertex:
    def __init__(self, id):
        self.id = id
        self.facts = {}

    def update_facts(self, facts: dict):
        self.facts = facts

    def __repr__(self):
        return "<Vertex({})>".format(self.id)


class Graph:

    def __init__(self):
        self.vertices = list()
        self.edges = {}
        self._index = {}

    def add_vertex(self, v: Vertex):
        """
        Adds the Vertex to the Graph.

        :param v:
        :return:
        """
        if isinstance(v, Vertex) and v not in self.vertices:
            self.vertices.append(v)
            self.edges[v] = {}
            self._index[v.id] = {}
            return True
        else:
            return False

    def add_edge(self, head: Vertex, tail: Vertex, weight: int = 0):
        """
        Adds edge between 2 vertexes

        :param head:
        :param tail:
        :param weight:
        :return:
        """
        if head and tail in self.vertices:
            self.edges[head][tail] = weight
            self.edges[tail][head] = weight

            self._index[head.id][tail.id] = weight
            self._index[tail.id][head.id] = weight
            return True
        else:
            return False

    def build(self):
        """
        Iterates through the Graph and builds text representation.

        :return:
        """
        graph = {}
        for vertex in self.edges.keys():
            graph[vertex.id] = []

            for edge in self.edges[vertex].items():
                node_id = edge[0].id
                weight = edge[1]

                graph[vertex.id].append((node_id, weight))

        return graph

    def get_edges(self, v):
        """
        Extracts the edges of the specified Vertex. Can be queried with
        either the Vertex object or Vertex.id

        :param v_id:
        :return:
        """
        if isinstance(v, str):
            if v in self._index.keys():
                return self._index[v]

        if isinstance(v, Vertex):
            if v in self.vertices:
                return self._index[v.id]

        return False

    def is_edge(self, head, tail) -> bool:
        """
        Validates if the provided tail vertex is an edge of the head.

        Can be queried with the Vertex object or Vertex ID.

        """
        if isinstance(head, Vertex) and isinstance(tail, Vertex):
            if head and tail in self.vertices:
                head_id = head.id
                tail_id = tail.id

                if tail_id in self._index[head_id]:
                    return True

        if isinstance(head, str) and isinstance(tail, str):
            if head and tail in self._index:
                h = self._index[head]
                if tail in h:
                    return True

        return False

    def display(self):
        G = nx.Graph(name="network_graph")

        graph = self.build()
        for head in graph.keys():
            for edge in graph[head]:
                edge_id = edge[0]
                weight = edge[1]

                G.add_edge(head, edge_id, weight=weight)

        pos = nx.spring_layout(G)  # positions for all nodes

        nx.draw_networkx(G, pos=pos)
        plt.show()

    def save(self, fname):
        G = nx.Graph()

        graph = self.build()
        for head in graph.keys():
            for edge in graph[head]:
                edge_id = edge[0]
                weight = edge[1]

                G.add_edge(head, edge_id, weight=weight)

        nx.draw_networkx(G)
        plt.savefig(fname)


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

    v1 = Vertex("R1")
    v2 = Vertex("R2")
    v3 = Vertex("R3")
    v4 = Vertex("R4")

    G.add_vertex(v1)
    G.add_vertex(v2)
    G.add_vertex(v3)
    G.add_vertex(v4)

    G.add_edge(v1, v2, 10)
    G.add_edge(v1, v3, 15)
    G.add_edge(v2, v3, 100)
    G.add_edge(v2, v4, 25)

    G.display()
    G.save("my_graph1.png")

    # print(G._index)
    # print(G.vertices)
    # print(v1, v2, v3, v4)


def test_pydot():
    G = nx.Graph(name="network_graph")

    v1 = Vertex("R1")
    v2 = Vertex("R2")
    v3 = Vertex("R3")
    v4 = Vertex("R4")

    G.add_edge(v1, v2, weight=15)
    G.add_edge(v1, v3, weight=15)
    G.add_edge(v1, v4, weight=15)

    print(G.nodes)

    print(G.edges)

    elarge = [(u, v) for (u, v, d) in G.edges(data=True)]
    esmall = [(u, v) for (u, v, d) in G.edges(data=True)]
    # pos = nx.spring_layout(G)  # positions for all nodes

    plt.figure()
    nx.draw_networkx(G)
    # print()

    #
    # nx.draw_networkx_nodes(G,  pos, node_size=700)
    #
    #
    # nx.draw_networkx_edges(
    #     G, pos, edgelist=esmall, width=6, alpha=0.5, edge_color="b", style="dashed"
    # )
    #
    # nx.draw_networkx_labels(G, pos, font_size=20, font_family="sans-serif")
    #
    plt.show()


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

        n1 = Vertex(hostname)
        n1.update_facts(fact)

        G.add_vertex(n1)

        time.sleep(1)

        for nbr in fact.get("nbrs"):
            for v in G.vertices:
                if nbr == v.facts.get("router_id"):
                    G.add_edge(n1, v, 1)

    print("\nResults:")
    G.display()
    print(G.build())


if __name__ == "__main__":
    main()
