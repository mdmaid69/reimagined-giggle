  import csv
  def read_csv_file(file_name):
        with open(file_name, "r") as file:
          return list(csv.reader(file))
import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))