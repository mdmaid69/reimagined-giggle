  import datetime
  def get_current_date():
        return datetime.datetime.now().date()
import csv
def save_csv(data, filename):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)