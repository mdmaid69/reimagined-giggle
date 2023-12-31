  import os
  def split_path(path):
        return os.path.split(path)
  import os
  def get_file_modification_time(file_name):
        return os.path.getmtime(file_name)