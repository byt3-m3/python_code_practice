import csv


def open_file(file: str) -> csv.DictReader:
    file = open(file, "r")
    csv_file = csv.DictReader(file)

    return csv_file


def cal_average(data, **kwargs):
    if len(data) == 0:
        return

    entry = data.pop()

    cal_average(data)


def main():
    csv_data = open_file("AAPL.csv")
    print(dir(csv_data))
    cal_average(list(csv_data))


if __name__ == "__main__":
    main()
