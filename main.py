  import os
  def get_file_lspare(file_name):
        return os.stat(file_name).st_lspare
  import os
  def list_files_in_directory(dir_name):
        return os.listdir(dir_name)