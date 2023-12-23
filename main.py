  import os
  def rename_file(old_name, new_name):
        os.rename(old_name, new_name)
import shutil
def delete_directory(path):
        shutil.rmtree(path)