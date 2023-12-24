  import os
  def get_file_device(file_name):
        return os.stat(file_name).st_dev
for i in range(10): print(i)