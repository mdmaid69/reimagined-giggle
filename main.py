  import os
  def get_file_gen(file_name):
        return os.stat(file_name).st_gen
n = 10
print("Powers of 2:", [2**x for x in range(n)])