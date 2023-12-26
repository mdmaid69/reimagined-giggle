import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)
  import os
  def get_absolute_path(file_name):
        return os.path.abspath(file_name)