  def calculate_perimeter_rectangle(l, w):
        return 2 * (l + w)
import csv
def read_csv_file(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)