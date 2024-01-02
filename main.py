  import os
  def get_file_mode(file_name):
        return os.stat(file_name).st_mode
def sort_numbers(numbers):
        return sorted(numbers)