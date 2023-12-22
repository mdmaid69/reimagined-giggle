import datetime
def get_today_date():
        return datetime.date.today()
import csv
def read_csv_file(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)