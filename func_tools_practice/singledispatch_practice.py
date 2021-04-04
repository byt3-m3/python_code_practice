from dataclasses import dataclass
from functools import singledispatch


@dataclass
class Router:
    hostname: str


@dataclass
class CiscoRouter(Router):
    vendor: str = "cisco"


@dataclass
class JuniperRouter(Router):
    vendor: str = "juniper"


@singledispatch
def process_router(router: Router):
    print("Processing Generatic Router")


@process_router.register
def _(router: CiscoRouter):
    print("Processing Cisco Router")


@process_router.register
def _(router: JuniperRouter):
    print("Processing Juniper Router")


def main():
    j_router = JuniperRouter(hostname="j1")
    c_router = CiscoRouter(hostname="c1")
    base_router = Router(hostname="b1")

    process_router(j_router)
    process_router(c_router)
    process_router(base_router)


if __name__ == "__main__":
    main()
