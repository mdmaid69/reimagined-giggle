  import os
  def get_base_name(path):
        return os.path.basename(path)
import shutil
def copy_file(src, dst):
        shutil.copy(src, dst)