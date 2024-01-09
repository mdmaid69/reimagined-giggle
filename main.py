import csv
def write_csv_file(filename, data):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)
  def calculate_circumference_circle(r):
        return 2 * 3.14 * r