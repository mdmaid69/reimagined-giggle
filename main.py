  import os
  def get_file_creation_time(file_name):
        return os.path.getctime(file_name)
n = 10
print("Powers of 2:", [2**x for x in range(n)])