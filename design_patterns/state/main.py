import abc


class State(metaclass=abc.ABCMeta):

    @abc.abstractstaticmethod
    def handle():
        pass


class Context:

    def __init__(self, state: State):
        self._state = state

    def run(self):
        return self._state.handle()

    def set_state(self, state):
        # print(state)
        self._state = state


class OnState(State):
    @staticmethod
    def handle():
        return "Lights On"


class OffState(State):
    @staticmethod
    def handle():
        return "Lights Off"


class LightSwitchContext(Context):
    def __init__(self):
        super().__init__(OffState)


    def switch(self):

        if self._state is OffState:
            self.set_state(OnState)
            return self.run()

        if self._state is OnState:
            self.set_state(OffState)
            return self.run()


def main():
    light_switch = LightSwitchContext()
    while True:

        cmd = input("Press Enter to toggle lights | Type e to exit: ")
        if cmd == "e":
            exit()

        print(light_switch.switch())
        # print(light_switch._state)


if __name__ == "__main__":
    main()
