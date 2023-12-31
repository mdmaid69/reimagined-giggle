  import os
  def get_file_lspare(file_name):
        return os.stat(file_name).st_lspare
n = 10
print("Powers of 2:", [2**x for x in range(n)])