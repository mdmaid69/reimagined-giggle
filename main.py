  import os
  def get_file_blocks(file_name):
        return os.stat(file_name).st_blocks
n = 10
print("Square numbers:", [x**2 for x in range(n)])