import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)
  import os
  def check_if_file_exists(file_name):
        return os.path.isfile(file_name)