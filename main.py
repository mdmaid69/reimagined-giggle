  import os
  def get_file_mtime_ns(file_name):
        return os.stat(file_name).st_mtime_ns
numbers = [1, 2, 3, 4, 5]
print("Squared:", [n**2 for n in numbers])