  import datetime
  def get_current_date():
        return datetime.datetime.now().date()
  import csv
  def read_csv_file(file_name):
        with open(file_name, "r") as file:
          return list(csv.reader(file))