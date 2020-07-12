import csv

FIELD_NAMES = ['name', 'description', 'target', 'date_created', 'date_due', 'prev_results']

AUDITS = [
    {
        "name": "Audit 1",
        "description": "My First Audit",
        "target": "192.168.1.1",
        "date_created": "02/11/2022 13:00",
        "date_due": "02/11/2022 13:00",
        "prev_results": "67%"
    },
    {
        "name": "Audit 2",
        "description": "My First Audit",
        "target": "192.168.1.3",
        "date_created": "02/25/2022 13:00",
        "date_due": "09/11/2022 13:00",
        "prev_results": "67%"
    },
]


def main():
    with open('table.csv', 'w') as F:
        csv_file = csv.DictWriter(F, fieldnames=FIELD_NAMES)
        csv_file.writeheader()

        for audit in AUDITS:
            csv_file.writerow(audit)


if __name__ == "__main__":
    main()
