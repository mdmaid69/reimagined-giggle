  import os
  def get_file_flags(file_name):
        return os.stat(file_name).st_flags
def find_min(numbers):
        return min(numbers)