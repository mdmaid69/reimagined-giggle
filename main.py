import os
def get_file_modification_time(filename):
        return os.path.getmtime(filename)
  import os
  def get_file_access_time(file_name):
        return os.path.getatime(file_name)