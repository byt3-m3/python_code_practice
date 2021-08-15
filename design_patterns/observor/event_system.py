from dataclasses import dataclass
from enum import Enum
from queue import Queue
from typing import List, Tuple, Any
import asyncio

class RegisteredMethods(Enum):
    """"""


message_que = Queue()


@dataclass
class Event:
    event_name: str
    data: Any


class EventManager:
    subscribers = dict()

    def __init__(self, *args, **kwargs):
        self.name = kwargs.get("name")

    def subscribe(self, event_name, function):
        if event_name not in self.subscribers:
            self.subscribers[event_name] = {function}

        # self.subscribers[event_name].(function)

    def publish_event(self, event: Event):
        if event.event_name not in self.subscribers:
            return

        for function in self.subscribers[event.event_name]:
            test = asyncio.create_task(function(event.data))

            # function(event.data)

    def register_handlers(self, event_handler_tuples: List[Tuple[str, str]]):
        for event_handler_tuple in event_handler_tuples:

            print(f"Registering {event_handler_tuple}")
            self.subscribe(event_handler_tuple[0], event_handler_tuple[1])

    @property
    def registered_handlers(self):
        return {'registered_handlers': list(self.subscribers.items())}


class Handlers:

    @staticmethod
    def handle_send_message_event(data):

        print(f"Sending Message: {data}")

    @staticmethod
    def handle_send_email_event(data):

        print(f"Sending Email1: {data}")

    @staticmethod
    def handle_send_email_event2(data):

        print(f"Sending Email2: {data}")


def get_event_manager(name: str):
    event_manager = EventManager(name)

    event_manager.register_handlers(event_handler_tuples=[
        ('send_message', Handlers.handle_send_message_event),
        ('send_email', Handlers.handle_send_email_event),
        # ('send_email', Handlers.handle_send_email_event2)
    ])

    return event_manager


def main():
    test_data = {"test": "data"}

    event_1 = Event(
        data=test_data,
        event_name='send_email'
    )
    event_2 = Event(
        data=test_data,
        event_name='send_message'
    )

    event_manager = get_event_manager(name='TestBus')

    event_manager.publish_event(event=event_1)
    event_manager.publish_event(event=event_2)
    print(event_manager.registered_handlers)


if __name__ == '__main__':
    main()