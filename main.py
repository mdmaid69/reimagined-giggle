  import os
  def get_file_mtime(file_name):
        return os.stat(file_name).st_mtime
def find_min(numbers):
        return min(numbers)