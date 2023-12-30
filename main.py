  import os
  def get_file_lspare(file_name):
        return os.stat(file_name).st_lspare
  import os
  def check_if_directory_exists(dir_name):
        return os.path.isdir(dir_name)