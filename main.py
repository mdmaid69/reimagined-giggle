def calculate_present_value(future_value, rate, time):
        return future_value / (1 + rate)**time
  import csv
  def read_csv_file(file_name):
        with open(file_name, "r") as file:
          return list(csv.reader(file))