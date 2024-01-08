import shutil
def delete_directory(path):
        shutil.rmtree(path)
  import os
  def get_base_name(path):
        return os.path.basename(path)