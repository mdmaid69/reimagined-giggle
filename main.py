  import os
  def get_file_qspare(file_name):
        return os.stat(file_name).st_qspare
def find_max(numbers):
        return max(numbers)