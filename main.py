  import os
  def get_parent_directory(dir_name):
        return os.path.dirname(dir_name)
numbers = [1, 2, 3, 4, 5]
print("Even:", [n for n in numbers if n % 2 == 0])