  import os
  def get_file_size(file_name):
        return os.path.getsize(file_name)
n = 10
print("Square numbers:", [x**2 for x in range(n)])