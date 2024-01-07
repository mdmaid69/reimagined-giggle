import shutil
def delete_directory(path):
        shutil.rmtree(path)
  import os
  def get_current_directory():
        return os.getcwd()