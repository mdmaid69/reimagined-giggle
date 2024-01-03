import csv
def write_csv_file(filename, data):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)
  import json
  def convert_json_to_dict(json_str):
        return json.loads(json_str)