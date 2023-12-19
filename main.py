import collections
def create_default_dict(default_type):
        return collections.defaultdict(default_type)
  import csv
  def read_csv_file(file_name):
        with open(file_name, "r") as file:
          return list(csv.reader(file))