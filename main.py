def calculate_compound_interest(principal, rate, time):
        return principal * (1 + rate)**time - principal
  import csv
  def read_csv_file(file_name):
        with open(file_name, "r") as file:
          return list(csv.reader(file))