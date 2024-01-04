n = 10
print("Powers of 2:", [2**x for x in range(n)])
  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)