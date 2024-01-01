  def find_max(lst):
        return max(lst) if len(lst) != 0 else "List is empty"
import csv
def load_csv(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)