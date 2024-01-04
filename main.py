  import os
  def get_current_directory():
        return os.getcwd()
  import os
  def create_directory(dir_name):
        os.makedirs(dir_name, exist_ok=True)