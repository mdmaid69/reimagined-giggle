  import os
  def get_file_atime(file_name):
        return os.stat(file_name).st_atime
  import os
  def list_files_in_directory(dir_name):
        return os.listdir(dir_name)