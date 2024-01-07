  import os
  def get_file_access_time(file_name):
        return os.path.getatime(file_name)
  import os
  def list_files_in_directory(dir_name):
        return os.listdir(dir_name)