  import os
  def get_file_blocks(file_name):
        return os.stat(file_name).st_blocks
import shutil
def delete_directory(path):
        shutil.rmtree(path)