import shutil
def move_file(src, dst):
        shutil.move(src, dst)
  import os
  def get_base_name(path):
        return os.path.basename(path)