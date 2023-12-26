numbers = [1, 2, 3, 4, 5]
print("Even:", [n for n in numbers if n % 2 == 0])
  import os
  def check_if_file_exists(file_name):
        return os.path.isfile(file_name)