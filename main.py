  import csv
  def read_csv_file(file_name):
        with open(file_name, "r") as file:
          return list(csv.reader(file))
import itertools
def get_permutations(iterable):
        return list(itertools.permutations(iterable))