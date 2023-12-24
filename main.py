  import os
  def get_file_mode(file_name):
        return os.stat(file_name).st_mode
def calculate_average(numbers):
        return sum(numbers) / len(numbers)