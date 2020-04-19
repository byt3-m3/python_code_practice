"""
This Desin

"""

from weakref import WeakValueDictionary


class Singleton(type):
    # Uses a WeakValueDictionary to allow the ability to delete the Singleton in memory

    _instance = WeakValueDictionary()

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instance:

            instance = super(Singleton, cls).__call__(*args, **kwargs)
            cls._instance[cls] = instance
            print([key for key in cls._instance.values()])

        return cls._instance[cls]


class Dispatcher(metaclass=Singleton):
    def __init__(self, **data):
        self.name = data.get("name")


def main():

    d1 = Dispatcher(name="john")
    # del d1
    d1 = Dispatcher(name="test")
    # print(d1.name, d1.name)
    # print(d1.name, d1.name)
    print(d1.name)
    print(d1 is d1)
    print(type(d1))


if __name__ == "__main__":
    main()
