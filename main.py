  import json
  def convert_json_to_dict(json_str):
        return json.loads(json_str)
import csv
def read_csv_file(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)