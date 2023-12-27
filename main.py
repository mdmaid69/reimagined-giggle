  import csv
  def write_to_csv_file(file_name, data):
        with open(file_name, "w", newline="") as file:
          writer = csv.writer(file)
          writer.writerows(data)
import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)