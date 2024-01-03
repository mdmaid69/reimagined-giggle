import csv
def write_csv_file(filename, data):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)
  import re
  def find_all_occurrences(pattern, string):
        return re.findall(pattern, string)