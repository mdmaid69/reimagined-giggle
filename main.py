  import datetime
  def get_current_date():
        return datetime.datetime.now().date()
import csv
def write_csv_file(filename, data):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)