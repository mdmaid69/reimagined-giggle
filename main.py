import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)
  import os
  def delete_directory(dir_name):
        os.rmdir(dir_name)