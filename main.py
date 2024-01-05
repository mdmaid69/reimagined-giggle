  import csv
  def read_csv_file(file_name):
        with open(file_name, "r") as file:
          return list(csv.reader(file))
import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)