  import os
  def get_parent_directory(dir_name):
        return os.path.dirname(dir_name)
  import os
  def create_directory(dir_name):
        os.makedirs(dir_name, exist_ok=True)