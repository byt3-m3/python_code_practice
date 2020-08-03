'''
The Command pattern is pretty common in Python code. Most often it’s used as an alternative for callbacks to
parameterizing UI elements with actions. It’s also used for queueing tasks, tracking operations history, etc.
'''
from abc import ABC, abstractmethod
import os


class CommandResult:
    def __init__(self, data, status: bool = False):
        self.data = data
        self.status = status

    def __repr__(self):
        return f'<CommandResult(status={self.status})>'


class ICommand(ABC):

    @abstractmethod
    def execute(self) -> CommandResult:
        raise NotImplementedError


class Command(ICommand):
    def __init__(self, **kwargs):
        self.cmd = kwargs.get("cmd")
        self.arg = kwargs.get("arg")
        self._run_log = []
        self._runs = 0

    def execute(self):
        raise NotImplementedError

    @property
    def run_count(self):
        """
        Returns the amount of times the ICommand.execute() method was called.
        """
        return len(self._run_log)

    @property
    def results(self):
        return self._run_log

    @results.setter
    def results(self, result: CommandResult):
        if isinstance(result, CommandResult):
            self._run_log.append(result)

    def __repr__(self):
        return f"<Command(cmd='{self.cmd}', arg='{self.arg}')>_run_count='{self.run_count}'"


class ComplexCommand(ICommand):
    def __init__(self, receiver, **kwargs):
        pass

    def execute(self):
        pass


class OSCommand(Command):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def execute(self):
        self._runs += 1
        res = os.popen(f'{self.cmd} {self.arg}').read()
        self.results = CommandResult(res, True)
        return self


def main():
    ping = OSCommand(cmd="ping", arg='8.8.8.8')
    nslookup = OSCommand(cmd="nslookup", arg='google.com')
    arp = OSCommand(cmd="arp", arg='-a')
    ping.execute()
    ping.execute()
    print(ping)
    print(ping.run_count)

    arp.execute()
    print(arp.results)
    print(arp.run_count)
    print(nslookup.run_count)
    print(nslookup.results)


if __name__ == "__main__":
    main()
