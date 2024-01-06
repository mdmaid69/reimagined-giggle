def calculate_volume(length, width, height):
        return length * width * height
  import csv
  def read_csv_file(file_name):
        with open(file_name, "r") as file:
          return list(csv.reader(file))