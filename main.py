  import os
  def check_if_file_exists(file_name):
        return os.path.isfile(file_name)
numbers = [1, 2, 3, 4, 5]
print("Squared:", [n**2 for n in numbers])