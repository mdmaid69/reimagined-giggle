  import os
  def get_file_mtime(file_name):
        return os.stat(file_name).st_mtime
for i in range(10): print(i)