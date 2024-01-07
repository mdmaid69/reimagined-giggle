  import json
  def convert_json_to_dict(json_str):
        return json.loads(json_str)
import csv
def save_csv(data, filename):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)