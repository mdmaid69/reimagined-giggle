  import csv
  def read_csv_file(file_name):
        with open(file_name, "r") as file:
          return list(csv.reader(file))
import json
def convert_to_json(data):
        return json.dumps(data)