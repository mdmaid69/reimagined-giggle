  def calculate_area_circle(r):
        return 3.14 * r**2
import csv
def load_csv(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)