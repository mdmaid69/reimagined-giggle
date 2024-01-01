  import os
  def get_file_modification_time(file_name):
        return os.path.getmtime(file_name)
numbers = [1, 2, 3, 4, 5]
print("Even:", [n for n in numbers if n % 2 == 0])