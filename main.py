  import os
  def get_absolute_path(file_name):
        return os.path.abspath(file_name)
numbers = [1, 2, 3, 4, 5]
print("Even:", [n for n in numbers if n % 2 == 0])