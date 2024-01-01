def calculate_average(numbers):
        return sum(numbers) / len(numbers)
  import os
  def get_file_size(file_name):
        return os.stat(file_name).st_size