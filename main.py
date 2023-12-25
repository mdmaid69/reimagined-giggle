  import os
  def get_file_dev(file_name):
        return os.stat(file_name).st_dev
for i in range(5):
        print(i)