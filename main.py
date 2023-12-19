import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()
  import csv
  def write_to_csv_file(file_name, data):
        with open(file_name, "w", newline="") as file:
          writer = csv.writer(file)
          writer.writerows(data)