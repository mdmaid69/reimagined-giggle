def calculate_speed(distance, time):
        return distance / time
  import csv
  def read_csv_file(file_name):
        with open(file_name, "r") as file:
          return list(csv.reader(file))