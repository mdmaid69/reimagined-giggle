  import os
  def get_file_nlink(file_name):
        return os.stat(file_name).st_nlink
for i in range(10): print(i)