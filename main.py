import collections
def create_default_dict(default_type):
        return collections.defaultdict(default_type)
  import csv
  def write_to_csv_file(file_name, data):
        with open(file_name, "w", newline="") as file:
          writer = csv.writer(file)
          writer.writerows(data)