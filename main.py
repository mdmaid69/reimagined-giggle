def calculate_energy(mass, c=3*10**8):
        return mass * c**2
  import csv
  def read_csv_file(file_name):
        with open(file_name, "r") as file:
          return list(csv.reader(file))