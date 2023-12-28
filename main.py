  import os
  def get_file_ctime(file_name):
        return os.stat(file_name).st_ctime
def calculate_average(numbers):
        return sum(numbers) / len(numbers)