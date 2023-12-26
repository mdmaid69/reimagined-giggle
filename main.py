import csv
def load_csv(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)
  def calculate_perimeter_rectangle(l, w):
        return 2 * (l + w)