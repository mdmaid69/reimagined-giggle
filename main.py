  import os
  def create_directory(dir_name):
        os.makedirs(dir_name, exist_ok=True)
  import os
  def get_file_creation_time(file_name):
        return os.path.getctime(file_name)