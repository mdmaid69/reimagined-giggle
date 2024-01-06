def calculate_density(mass, volume):
        return mass / volume
  import csv
  def read_csv_file(file_name):
        with open(file_name, "r") as file:
          return list(csv.reader(file))