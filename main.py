  def find_min(lst):
        return min(lst) if len(lst) != 0 else "List is empty"
import csv
def write_csv_file(filename, data):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)