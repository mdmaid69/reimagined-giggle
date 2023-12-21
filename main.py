import csv
def save_csv(data, filename):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)
  import json
  def convert_dict_to_json(d):
        return json.dumps(d)