  import os
  def get_file_modification_time(file_name):
        return os.path.getmtime(file_name)
  import os
  def get_parent_directory(dir_name):
        return os.path.dirname(dir_name)