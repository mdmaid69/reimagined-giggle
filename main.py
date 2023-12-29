import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)
  import csv
  def read_csv_file(file_name):
        with open(file_name, "r") as file:
          return list(csv.reader(file))