  import os
  def get_file_number_of_links(file_name):
        return os.stat(file_name).st_nlink
def sort_numbers(numbers):
        return sorted(numbers)