def calculate_area_circle(r):
        return 3.14 * r**2
  import csv
  def read_csv_file(file_name):
        with open(file_name, "r") as file:
          return list(csv.reader(file))