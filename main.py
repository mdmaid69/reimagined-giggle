import os
def get_file_size(filename):
        return os.path.getsize(filename)
  import os
  def get_file_access_time(file_name):
        return os.path.getatime(file_name)