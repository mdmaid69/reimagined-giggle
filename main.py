  import os
  def get_file_blocks(file_name):
        return os.stat(file_name).st_blocks
n = 10
print("Cube numbers:", [x**3 for x in range(n)])