  def divide_numbers(x, y):
        return x / y if y != 0 else "Cannot divide by zero"
  import csv
  def read_csv_file(file_name):
        with open(file_name, "r") as file:
          return list(csv.reader(file))