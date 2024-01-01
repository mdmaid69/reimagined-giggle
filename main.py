  import re
  def find_all_occurrences(pattern, string):
        return re.findall(pattern, string)
import csv
def load_csv(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)