  import os
  def get_file_modification_time(file_name):
        return os.path.getmtime(file_name)
  import os
  def create_directory(dir_name):
        os.makedirs(dir_name, exist_ok=True)