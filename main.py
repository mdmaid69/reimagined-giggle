  import os
  def get_parent_directory(dir_name):
        return os.path.dirname(dir_name)
  import os
  def get_file_creation_time(file_name):
        return os.path.getctime(file_name)