  import os
  def get_directory_name(path):
        return os.path.dirname(path)
numbers = [1, 2, 3, 4, 5]
print("Even:", [n for n in numbers if n % 2 == 0])