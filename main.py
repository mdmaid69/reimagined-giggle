  import os
  def get_file_group(file_name):
        return os.stat(file_name).st_gid
  import os
  def create_directory(dir_name):
        os.makedirs(dir_name, exist_ok=True)