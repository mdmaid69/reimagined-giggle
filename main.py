import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)
  import os
  def get_directory_name(path):
        return os.path.dirname(path)