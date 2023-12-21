def calculate_future_value(principal, rate, time):
        return principal * (1 + rate)**time
  import csv
  def write_to_csv_file(file_name, data):
        with open(file_name, "w", newline="") as file:
          writer = csv.writer(file)
          writer.writerows(data)