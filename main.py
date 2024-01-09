  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)
def calculate_average(numbers):
        return sum(numbers) / len(numbers)