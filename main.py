  def divide_numbers(x, y):
        return x / y if y != 0 else "Cannot divide by zero"
import csv
def write_csv_file(filename, data):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)