  import os
  def get_file_size(file_name):
        return os.stat(file_name).st_size
  import os
  def get_file_modification_time(file_name):
        return os.path.getmtime(file_name)