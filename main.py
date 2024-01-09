import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)
  import os
  def get_base_name(path):
        return os.path.basename(path)