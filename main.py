  import json
  def convert_dict_to_json(d):
        return json.dumps(d)
import csv
def write_csv_file(filename, data):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)