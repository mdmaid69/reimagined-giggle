  import os
  def get_file_size_in_bytes(file_name):
        return os.stat(file_name).st_size
numbers = [1, 2, 3, 4, 5]
print("Even:", [n for n in numbers if n % 2 == 0])