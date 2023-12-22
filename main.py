  import os
  def rename_file(old_name, new_name):
        os.rename(old_name, new_name)
n = 10
print("Powers of 2:", [2**x for x in range(n)])