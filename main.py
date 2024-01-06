def calculate_circumference_circle(r):
        return 2 * 3.14 * r
  import csv
  def read_csv_file(file_name):
        with open(file_name, "r") as file:
          return list(csv.reader(file))