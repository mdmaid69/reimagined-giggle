  import os
  def get_file_size(file_name):
        return os.stat(file_name).st_size
for i in range(5):
        print(i)