import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))
  import csv
  def read_csv_file(file_name):
        with open(file_name, "r") as file:
          return list(csv.reader(file))