  import os
  def delete_directory(dir_name):
        os.rmdir(dir_name)
def calculate_average(numbers):
        return sum(numbers) / len(numbers)