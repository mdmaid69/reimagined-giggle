  import os
  def get_file_atime_ns(file_name):
        return os.stat(file_name).st_atime_ns
  import os
  def list_files_in_directory(dir_name):
        return os.listdir(dir_name)