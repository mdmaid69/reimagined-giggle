  import csv
  def read_csv_file(file_name):
        with open(file_name, "r") as file:
          return list(csv.reader(file))
import heapq
def merge_sorted_iterables(*iterables):
        return heapq.merge(*iterables)