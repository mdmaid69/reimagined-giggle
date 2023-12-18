  import csv
  def read_csv_file(file_name):
        with open(file_name, "r") as file:
          return list(csv.reader(file))
import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)