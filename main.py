for i in range(10): print(i)
  import os
  def get_file_mode(file_name):
        return os.stat(file_name).st_mode