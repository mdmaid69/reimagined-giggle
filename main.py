  import os
  def get_file_ctime_ns(file_name):
        return os.stat(file_name).st_ctime_ns
import csv
with open("some.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["spam", "eggs", "bacon", "ham"])
        writer.writerow(["Hello, world!", "eggs", "bacon", "ham"])