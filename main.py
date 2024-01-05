  import json
  def convert_json_to_dict(json_str):
        return json.loads(json_str)
import csv
def load_csv(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)