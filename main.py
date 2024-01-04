import csv
def read_csv_file(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)
  import json
  def convert_dict_to_json(d):
        return json.dumps(d)