import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)
  import csv
  def write_to_csv_file(file_name, data):
        with open(file_name, "w", newline="") as file:
          writer = csv.writer(file)
          writer.writerows(data)