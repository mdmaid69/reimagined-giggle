import json
def read_from_json(json_string):
        return json.loads(json_string)
  import csv
  def read_csv_file(file_name):
        with open(file_name, "r") as file:
          return list(csv.reader(file))