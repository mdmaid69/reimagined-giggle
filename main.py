  import os
  def get_file_mtime(file_name):
        return os.stat(file_name).st_mtime
def find_max(numbers):
        return max(numbers)