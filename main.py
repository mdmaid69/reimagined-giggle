  import os
  def get_file_gen(file_name):
        return os.stat(file_name).st_gen
def sort_numbers(numbers):
        return sorted(numbers)