import shutil
def delete_directory(path):
        shutil.rmtree(path)
  import os
  def create_directory(dir_name):
        os.makedirs(dir_name, exist_ok=True)