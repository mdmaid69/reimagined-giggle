  import os
  def delete_directory(dir_name):
        os.rmdir(dir_name)
  import os
  def create_directory(dir_name):
        os.makedirs(dir_name, exist_ok=True)