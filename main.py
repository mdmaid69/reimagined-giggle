  import os
  def get_file_block_size(file_name):
        return os.stat(file_name).st_blksize
import csv
def save_csv(data, filename):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)