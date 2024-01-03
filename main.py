  import os
  def get_file_ctime(file_name):
        return os.stat(file_name).st_ctime
for i in range(5):
        print(i)