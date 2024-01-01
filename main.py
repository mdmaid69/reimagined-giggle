  def find_max(lst):
        return max(lst) if len(lst) != 0 else "List is empty"
import csv
def read_csv_file(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)