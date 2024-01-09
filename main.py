import datetime
def get_current_date():
        return datetime.date.today()
import csv
def load_csv(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)