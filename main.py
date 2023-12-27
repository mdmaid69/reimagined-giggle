import csv
def load_csv(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)
  def calculate_circumference_circle(r):
        return 2 * 3.14 * r