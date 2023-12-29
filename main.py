import csv
def load_csv(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)
import datetime
def get_today_date():
        return datetime.date.today()