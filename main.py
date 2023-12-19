  import os
  def get_file_extension(file_name):
        return os.path.splitext(file_name)[1]
import csv
with open("some.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["spam", "eggs", "bacon", "ham"])
        writer.writerow(["Hello, world!", "eggs", "bacon", "ham"])