  import csv
  def read_csv_file(file_name):
        with open(file_name, "r") as file:
          return list(csv.reader(file))
  import json
  def convert_dict_to_json(d):
        return json.dumps(d)