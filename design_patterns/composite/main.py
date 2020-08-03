'''
Composite became a pretty popular solution for the most problems that require building a tree structure.
Composite’s great feature is the ability to run methods recursively over the whole tree structure and sum up the
results.
'''
from typing import List
from abc import ABC, abstractmethod


class Component(ABC):

    @abstractmethod
    def execute(self) -> any:
        """
        The base Component may implement some default behavior or leave it to
        concrete classes (by declaring the method containing the behavior as
        "abstract").
        """

        pass


class Leaf(Component):
    def __init__(self, id=None):
        self._id = id

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, component: Component):
        if isinstance(component, Component):
            self._parent = component

    def execute(self) -> any:
        pass

    def __repr__(self):
        return f'<Leaf(id={self._id})>'


class Composite(Component):
    def __init__(self, id=None):
        self._parent = None
        self._id = id
        self._children = []

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, component: Component):
        if isinstance(component, Component):
            self._parent = component

    @property
    def children(self):
        return self._children

    @children.setter
    def children(self, component: Component):
        if isinstance(component, Component):
            component.parent = self
            self._children.append(component)

    def execute(self) -> any:
        pass

    def __repr__(self):
        return f'<Composite(id={self._id}, children={[child for child in self.children]})>'


def main():
    c1 = Composite("top")
    c2 = Composite("l1br1")
    c3 = Composite("l1br2")
    c4 = Composite("l2br1")
    c5 = Composite("l2br2")

    l1 = Leaf('l1')
    l2 = Leaf('l2')

    c1.children = c2
    c1.children = c3

    c3.children = c4
    c3.children = c5

    c4.children = l1
    c5.children = l2

    print(c1.children)


if __name__ == "__main__":
    main()
