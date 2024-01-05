  import os
  def get_file_ctime(file_name):
        return os.stat(file_name).st_ctime
print(sum(range(10)))