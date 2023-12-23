import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)
  import os
  def get_parent_directory(dir_name):
        return os.path.dirname(dir_name)