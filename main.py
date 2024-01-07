  import csv
  def read_csv_file(file_name):
        with open(file_name, "r") as file:
          return list(csv.reader(file))
import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)