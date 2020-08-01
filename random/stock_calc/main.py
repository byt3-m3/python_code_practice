import csv


def reader():
    with open("AAPL.csv", "r") as f:
        reader = csv.DictReader(f)
        _sma = 0
        for row in reader:
            sma = None
            # print(reader)
            if row.get("Open") == row.get("Close"):
                print(row)
                print("Trade")
            # print(row)


reader()