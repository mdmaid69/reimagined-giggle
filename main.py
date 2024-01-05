import csv
def save_csv(data, filename):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)
  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)