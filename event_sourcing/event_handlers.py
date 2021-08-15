import json

from events import (
    CreateRouterEvent,
    ChangeRouterStatusEvent,
    SetRouterMaintenanceEvent,
    ChangeRouterHostnameEvent,
    DeleteRouterEvent,
    DecommRouterEvent,
)


class Router:

    def __init__(self, **kwargs):
        self.hostname = kwargs.get("hostname")
        self.status = kwargs.get("status")

    def __repr__(self):
        return f'Router(hostname={self.hostname}, status={self.status})'


class RouterDAO:
    def __init__(self):
        self._items = []

    @property
    def routers(self):
        return self._items

    def add_router(self, router: Router):
        if isinstance(router, Router):
            print(f"Adding {router.hostname}")
            self._items.append(router)

        self.to_file()

    def get_router_by_hostname(self, hostname) -> Router:
        for router in self._items:
            if router.hostname == hostname:
                return router

    def delete_router(self, hostname):
        router = self.get_router_by_hostname(hostname=hostname)
        self._items.remove(router)
        self.to_file()

    def to_file(self):
        with open("routersdb.json", "w") as file:
            json_data = json.dumps([item.__dict__ for item in self._items])
            file.write(json_data)


class RouterEventHandler:

    def __init__(self, dao: RouterDAO, events: list):
        self._events = events
        self.dao = dao

        self._routers = []

    @property
    def event_history(self):
        return [
            {
                "event_id": event.id,
                "event_type": event.type,
                "namespace": event.namespace,
                "created": event.created,
            } for event in self._events
        ]

    @property
    def last_event(self):
        return self._events[len(self._events) - 1]

    def process(self):
        for event in self._events:
            self._handle_event(event=event)

    def _handle_create_router(self, event: CreateRouterEvent):
        hostname = event.namespace.hostname
        status = event.namespace.status

        router = self.dao.get_router_by_hostname(hostname=event.namespace.hostname)
        if router:
            print(f"Unabled to Create Router: {hostname}, Hostname Exsists!")

        else:
            print(f"Creating Router: '{hostname}'")
            _router = Router(hostname=hostname, status=status)
            self.dao.add_router(router=_router)

    def _handle_delete_router(self, event: DeleteRouterEvent):
        hostname = event.namespace.hostname

        print(f"Removing Router: '{hostname}'")
        self.dao.delete_router(hostname=hostname)

    def _handle_change_router_hostname(self, event: ChangeRouterHostnameEvent):
        new_val = event.namespace.new_val
        hostname = event.namespace.hostname

        print(f"Changing Router '{hostname}' Hostname to: {new_val}")
        router = self.dao.get_router_by_hostname(hostname=hostname)
        router.hostname = new_val

    def _handle_change_router_status(self, event: ChangeRouterStatusEvent):
        hostname = event.namespace.hostname
        status = event.namespace.status

        print(f"Changing Router '{hostname}' Status to: {status}")
        router = self.dao.get_router_by_hostname(hostname=hostname)
        router.status = status

    def _handle_decommission_router(self, event: DecommRouterEvent):
        hostname = event.namespace.hostname

        print(f"Decommissioning Router '{hostname}'")
        router = self.dao.get_router_by_hostname(hostname=hostname)
        router.status = event.decommissioned_status

    def _handle_set_maintenance_model(self, event: SetRouterMaintenanceEvent):
        hostname = event.namespace.hostname

        print(f"Puting Router in maintennace Mode: '{hostname}'")
        router = self.dao.get_router_by_hostname(hostname=hostname)
        router.status = event.maintenance_status

    def _handle_event(self, event):
        self._event_handler_map = {
            CreateRouterEvent: {
                "handler": self._handle_create_router
            },
            DeleteRouterEvent: {
                "handler": self._handle_delete_router
            },
            ChangeRouterHostnameEvent: {
                "handler": self._handle_change_router_hostname
            },
            ChangeRouterStatusEvent: {
                "handler": self._handle_change_router_status
            },
            DecommRouterEvent: {
                "handler": self._handle_decommission_router
            },
            SetRouterMaintenanceEvent: {
                "handler": self._handle_set_maintenance_model
            },

        }

        handler = self._event_handler_map.get(type(event)).get("handler")

        handler(event=event)
        self.to_file()

    def process_event(self, event):
        self._handle_event(event)
        self._events.append(event)

    def to_file(self):
        with open("eventsdb.json", "w") as file:
            file.write(json.dumps([item.to_json() for item in self._events]))


def main():
    events = [
        CreateRouterEvent(hostname="R1", status="init"),
        CreateRouterEvent(hostname="R2", status="down"),
        CreateRouterEvent(hostname="R3", status="down"),
        CreateRouterEvent(hostname="R4", status="down"),
        CreateRouterEvent(hostname="R5", status="down"),
        CreateRouterEvent(hostname="R6", status="down"),
        ChangeRouterStatusEvent(hostname="R4", status='down'),
        ChangeRouterHostnameEvent(hostname="R1", new_val="R1-CHANGED"),
        ChangeRouterStatusEvent(hostname="R1-CHANGED", status="up"),
        ChangeRouterStatusEvent(hostname="R2", status="up"),
        ChangeRouterStatusEvent(hostname="R3", status="up"),
        ChangeRouterStatusEvent(hostname="R4", status="up"),

    ]

    event_handler = RouterEventHandler(dao=RouterDAO(), events=events)
    event_handler.process()
    event_handler.process_event(ChangeRouterHostnameEvent(hostname="R3", new_val="R3-CHANGED"))
    event_handler.process_event(SetRouterMaintenanceEvent(hostname="R2"))
    event_handler.process_event(DecommRouterEvent(hostname="R4"))
    event_handler.process_event(DeleteRouterEvent(hostname="R5"))

    print(event_handler.event_history)
    print(event_handler.last_event)
    print(event_handler.dao.routers)


if __name__ == '__main__':
    main()
