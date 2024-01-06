  import os
  def delete_file(file_name):
        os.remove(file_name)
n = 10
print("Powers of 2:", [2**x for x in range(n)])