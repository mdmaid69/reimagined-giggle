  import json
  def convert_dict_to_json(d):
        return json.dumps(d)
import csv
def load_csv(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)