  import os
  def get_file_rdev(file_name):
        return os.stat(file_name).st_rdev
def calculate_average(numbers):
        return sum(numbers) / len(numbers)