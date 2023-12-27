  import os
  def get_file_flags(file_name):
        return os.stat(file_name).st_flags
numbers = [1, 2, 3, 4, 5]
print("Even:", [n for n in numbers if n % 2 == 0])