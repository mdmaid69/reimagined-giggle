def calculate_average(numbers):
        return sum(numbers) / len(numbers)
  import os
  def create_directory(dir_name):
        os.makedirs(dir_name, exist_ok=True)