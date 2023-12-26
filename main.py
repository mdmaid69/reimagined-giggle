import shutil
def delete_directory(path):
        shutil.rmtree(path)
  import os
  def get_parent_directory(dir_name):
        return os.path.dirname(dir_name)