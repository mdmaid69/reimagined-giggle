  import csv
  def read_csv_file(file_name):
        with open(file_name, "r") as file:
          return list(csv.reader(file))
def calculate_simple_interest(principal, rate, time):
        return principal * rate * time