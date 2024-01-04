  import datetime
  def get_current_date():
        return datetime.datetime.now().date()
import csv
def read_csv_file(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)