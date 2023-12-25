  import csv
  def read_csv_file(file_name):
        with open(file_name, "r") as file:
          return list(csv.reader(file))
import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)