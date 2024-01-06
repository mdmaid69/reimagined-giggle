  import os
  def get_file_size_in_bytes(file_name):
        return os.stat(file_name).st_size
  import os
  def list_files_in_directory(dir_name):
        return os.listdir(dir_name)