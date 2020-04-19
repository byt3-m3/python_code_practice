from abc import ABC


class IObserver(ABC):
    def update(self):
        pass


class IObservable(ABC):
    def add(self, observer: IObserver):
        pass

    def remove(self, observer: IObserver):
        pass

    def notify(self):
        pass


class WeatherStation(IObservable):
    observers = []

    def __init__(self, **kwargs):
        self.temp = 0

    def add(self, observer: IObserver):
        if isinstance(observer, IObserver) and observer not in self.observers:
            self.observers.append(observer)
            return True
        else:
            return False

    def remove(self, observer: IObserver):
        if observer in self.observers:
            observer.clear()
            self.observers.remove(observer)

    def notify(self):

        if len(self.observers) > 0:
            for client in self.observers:
                client.update()
            return True

        return False

    def set_temp(self, temp: int):
        self.temp = temp

        self.notify()

    def get_temp(self):
        return self.temp


class PhoneDisplay(IObserver):
    def __init__(self, weather_station: WeatherStation):
        self.weather_station = weather_station
        self.curr_temp = 0

    def update(self):
        self.curr_temp = self.weather_station.get_temp()

    def clear(self):
        self.curr_temp = 0


class RSSServer(IObservable):
    def __init__(self):
        self.feeds = []
        self.clients = []

    def add(self, observer: IObserver):
        self.clients.append(observer)

    def new_feed(self, msg):
        self.feeds.append(msg)

        self.notify()

    def get_feeds(self):
        return self.feeds

    def notify(self):
        for client in self.clients:
            client.update()


class RSSClient(IObserver):
    def __init__(self, RSSServer: RSSServer):
        self.server = RSSServer
        self.feeds = []

    def update(self):
        self.feeds = self.server.get_feeds()

    def read(self):
        for feed in self.feeds:
            print(feed)


def example_rss():
    server = RSSServer()

    c1 = RSSClient(server)
    c2 = RSSClient(server)

    server.add(c1)
    server.add(c2)

    server.new_feed("Breaking News This works")

    print("Client1")
    c1.read()

    server.new_feed("Breaking News This Relly works")

    print("\nClient2")
    c2.read()


def example_weather():
    CR = WeatherStation()

    p1 = PhoneDisplay(CR)
    p2 = PhoneDisplay(CR)

    CR.add(p1)
    CR.add(p2)

    CR.set_temp(105)
    print(p1.curr_temp, p2.curr_temp)

    CR.remove(p2)

    CR.set_temp(95)
    print(p1.curr_temp, p2.curr_temp)


def main():
    example_rss()


if __name__ == "__main__":
    main()
