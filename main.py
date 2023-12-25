for i in range(5):
        print(i)
  import os
  def get_file_mtime(file_name):
        return os.stat(file_name).st_mtime