  def is_even(n):
        return n % 2 == 0
import csv
def read_csv_file(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)