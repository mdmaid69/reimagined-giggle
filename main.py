  import os
  def get_file_creation_time(file_name):
        return os.path.getctime(file_name)
  import os
  def list_files_in_directory(dir_name):
        return os.listdir(dir_name)