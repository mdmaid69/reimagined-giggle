  import os
  def get_file_birthtime(file_name):
        return os.stat(file_name).st_birthtime
def calculate_average(numbers):
        return sum(numbers) / len(numbers)