class _Device(type):
    @classmethod
    def __init__(self, class_name, bases, attrs):
        self.hostname = None
        print(class_name, bases, attrs)

    # def __new__(cls, class_name, bases, attrs):
    #     print(class_name, bases, attrs)
    #     _attrs = {}
    #     for key, val in attrs.items():
    #         if val.startswith("__"):
    #             print(key, val)
    #
    #     return type(class_name, bases, attrs)


class Device(metaclass=_Device):
    def __init__(self, **kwargs):
        super().__init__()

class Router(Device):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


def main():
    r1 = Router()
    # print(r1)
    print(r1)
    # print(type(Router))

    # assert type(Device), _Device


if __name__ == "__main__":
    main()
