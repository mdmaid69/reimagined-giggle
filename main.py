import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)
  import csv
  def write_to_csv_file(file_name, data):
        with open(file_name, "w", newline="") as file:
          writer = csv.writer(file)
          writer.writerows(data)