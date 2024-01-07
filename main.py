def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)
  import csv
  def read_csv_file(file_name):
        with open(file_name, "r") as file:
          return list(csv.reader(file))