import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)
  import csv
  def read_csv_file(file_name):
        with open(file_name, "r") as file:
          return list(csv.reader(file))