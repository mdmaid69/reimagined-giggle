import os
def list_files_in_directory(path):
        return os.listdir(path)
  import os
  def check_if_directory_exists(dir_name):
        return os.path.isdir(dir_name)