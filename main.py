def calculate_average(numbers):
        return sum(numbers) / len(numbers)
  import os
  def get_file_flags(file_name):
        return os.stat(file_name).st_flags