import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)
  import os
  def check_if_directory_exists(dir_name):
        return os.path.isdir(dir_name)