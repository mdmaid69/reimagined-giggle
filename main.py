import os
def get_file_modification_time(filename):
        return os.path.getmtime(filename)
  import os
  def get_parent_directory(dir_name):
        return os.path.dirname(dir_name)