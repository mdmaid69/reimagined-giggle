  import csv
  def write_to_csv_file(file_name, data):
        with open(file_name, "w", newline="") as file:
          writer = csv.writer(file)
          writer.writerows(data)
import re
def find_all_occurrences(pattern, string):
        return re.findall(pattern, string)