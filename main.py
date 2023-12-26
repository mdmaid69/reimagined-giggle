def calculate_average(numbers):
        return sum(numbers) / len(numbers)
  import os
  def get_file_number_of_links(file_name):
        return os.stat(file_name).st_nlink