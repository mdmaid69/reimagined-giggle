  import os
  def get_file_nlink(file_name):
        return os.stat(file_name).st_nlink
def find_min(numbers):
        return min(numbers)