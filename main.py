  import os
  def check_if_directory_exists(dir_name):
        return os.path.isdir(dir_name)
numbers = [1, 2, 3, 4, 5]
print("Even:", [n for n in numbers if n % 2 == 0])