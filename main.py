for i in range(10): print(i)
  import os
  def get_file_rdev(file_name):
        return os.stat(file_name).st_rdev