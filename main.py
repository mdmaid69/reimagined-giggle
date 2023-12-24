import csv
def save_csv(data, filename):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)
  import os
  def get_file_extension(file_name):
        return os.path.splitext(file_name)[1]