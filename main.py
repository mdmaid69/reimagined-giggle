import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)
  import os
  def list_files_in_directory(dir_name):
        return os.listdir(dir_name)