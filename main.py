  import os
  def get_file_name_without_extension(file_name):
        return os.path.splitext(file_name)[0]
n = 10
print("Powers of 2:", [2**x for x in range(n)])