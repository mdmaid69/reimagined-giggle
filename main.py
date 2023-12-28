  import os
  def get_file_ino(file_name):
        return os.stat(file_name).st_ino
  import os
  def create_directory(dir_name):
        os.makedirs(dir_name, exist_ok=True)