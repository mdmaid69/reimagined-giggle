  def divide_numbers(x, y):
        return x / y if y != 0 else "Cannot divide by zero"
import csv
def read_csv_file(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)