'''
This excerise is an example of utilizing LinkList in Python.

Linked-List vs Arrays(List)

- Insertion/Deletion for LinkedList is O(1)
- Element Access for LinkList is O(n)
- The Object is not Contiguous in Memory
'''


class Router:
    """
    Test Object to be used to be appended to LinkedList

    """

    def __init__(self, hostname=None):
        self.hostname = hostname

    def __repr__(self):
        return f'<Router(hostname={self.hostname})>'


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        '''
        This Method appends new data to the LinkedList object

        :param data:
        :return:
        '''
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next

        last_node.next = new_node
        return

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head

        self.head = new_node

    def length(self):
        """
        returns the total number of elements currently in the linked list.

        :return:
        """
        cur_node = self.head
        index = 0
        while cur_node:
            index += 1
            cur_node = cur_node.next

        return index

    def items(self):
        """
        Returns a List of Node data.

        :return:
        """
        elems = []
        cur_node = self.head
        while cur_node:
            elems.append(cur_node.data)
            cur_node = cur_node.next

        return elems

    def get(self, index):
        if index >= self.length():
            raise Exception("Index Out of Range")

        cur_index = 0
        cur_node = self.head

        while True:
            cur_node = cur_node.next
            if cur_index == index:
                return cur_node.data
            cur_index += 1

    def erase(self, index):
        if index >= self.length():
            raise Exception("Index Out of Range")

        cur_index = 0
        cur_node = self.head

        while True:
            last_node = cur_node
            cur_node = cur_node.next
            if cur_index == index:
                last_node.next = cur_node.next
                return True

            cur_index += 1

    def insert_after_node(self, prev_node, data):
        if not prev_node:
            raise Exception("Node Not In List")

        new_node = Node(data)

        new_node.next = prev_node.next
        prev_node.next = new_node

    def insert_after(self, index, data):
        if index > self.length():
            raise Exception("Index Out of Range")

        new_node = Node(data)

        cur_node = self.head
        cur_index = 0

        while cur_node:
            last_node = cur_node
            cur_node = cur_node.next

            if cur_index == index:
                new_node.next = cur_node
                last_node.next = new_node

            cur_index += 1


if __name__ == "__main__":
    # Creates a New Singly-Link List Object
    llist = LinkedList()

    # Appends Router object to the Linked List
    llist.append(Router("a"))
    llist.append(Router("b"))
    llist.append(Router("c"))
    llist.append(Router("d"))

    # llist.prepend(Router("test.bits.local"))

    llist.insert_after(2, Router("aa"))

    # llist.erase(0)

    print(llist.items())
    # print(llist.length())
    # print(results)
