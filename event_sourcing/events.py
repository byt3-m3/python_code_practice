import datetime
import uuid
from argparse import Namespace

VALID_ROUTER_STATUSES = ['up', 'down', 'decommed', 'maintenance']


class Event:
    def __init__(self, **kwargs):
        self.id = str(uuid.uuid4())
        self.type = kwargs.get("type")
        self.namespace = kwargs.get("namespace", Namespace())
        self.created = datetime.datetime.now().timestamp()

    def __repr__(self):
        return f"Event(id={self.id}, type={self.type}, namespace={self.namespace})"

    def to_json(self):
        return {
            "id": self.id,
            "type": self.type,
            "created": self.created,
            "namespace": self.namespace.__dict__,

        }


class CreateRouterEvent(Event):
    def __init__(self, hostname, status):
        super().__init__(
            type="router::create",
            namespace=Namespace(
                hostname=hostname,
                status=status
            )
        )


class DeleteRouterEvent(Event):
    def __init__(self, hostname):
        super().__init__(
            type="router::delete",
            namespace=Namespace(
                hostname=hostname
            )
        )
        self.hostname = hostname


class ChangeRouterStatusEvent(Event):

    def __init__(self, hostname, status):
        super().__init__(
            type="router:change_status",
            namespace=Namespace(
                hostname=hostname,
                status=status if status in VALID_ROUTER_STATUSES else 'down'
            )
        )


class ChangeRouterHostnameEvent(Event):
    def __init__(self, hostname, new_val):
        super().__init__(
            type="router::change_hostname",
            namespace=Namespace(
                hostname=hostname,
                new_val=new_val
            )
        )


class DecommRouterEvent(Event):
    def __init__(self, hostname):
        super().__init__(
            type="router::decommission",
            namespace=Namespace(
                hostname=hostname
            )
        )
        self.decommissioned_status = 'decommed'


class SetRouterMaintenanceEvent(Event):
    def __init__(self, hostname):
        super().__init__(
            type="router::set_mainetance_mode",
            namespace=Namespace(
                hostname=hostname
            )
        )

        self.hostname = hostname
        self.maintenance_status = 'maintenance'
