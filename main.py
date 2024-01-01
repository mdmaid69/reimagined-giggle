import shutil
def delete_directory(path):
        shutil.rmtree(path)
  import os
  def list_files_in_directory(dir_name):
        return os.listdir(dir_name)