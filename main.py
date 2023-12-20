  import csv
  def read_csv_file(file_name):
        with open(file_name, "r") as file:
          return list(csv.reader(file))
import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()