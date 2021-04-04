import attr

@attr.attrs()
class Router:
    hostname: str = attr.attrib()
    vendor: str = attr.attrib(default='cisco')


class NRouter:
    def __init__(self, *arg, **kwargs):
        self.hostname = kwargs.get("hostname")

def main():
    r1 = Router(hostname='hostname')
    r2 = NRouter()
    print(dir(r1))
    print(dir(r2))


if __name__ == "__main__":
    main()
