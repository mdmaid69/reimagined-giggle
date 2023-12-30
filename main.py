def calculate_force(mass, acceleration):
        return mass * acceleration
  import csv
  def read_csv_file(file_name):
        with open(file_name, "r") as file:
          return list(csv.reader(file))