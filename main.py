  import os
  def get_file_size_in_bytes(file_name):
        return os.stat(file_name).st_size
n = 10
print("Cube numbers:", [x**3 for x in range(n)])