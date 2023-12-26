  import os
  def get_file_rdev(file_name):
        return os.stat(file_name).st_rdev
  import os
  def list_files_in_directory(dir_name):
        return os.listdir(dir_name)