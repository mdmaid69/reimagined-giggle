for i in range(10): print(i)
  import os
  def get_file_access_time(file_name):
        return os.path.getatime(file_name)