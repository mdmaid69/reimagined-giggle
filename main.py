  import os
  def change_current_working_directory(dir_name):
        os.chdir(dir_name)
import shutil
def delete_directory(path):
        shutil.rmtree(path)