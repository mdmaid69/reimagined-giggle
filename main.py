  import os
  def get_file_modification_time(file_name):
        return os.path.getmtime(file_name)
  import os
  def get_file_atime(file_name):
        return os.stat(file_name).st_atime