  import os
  def get_base_name(path):
        return os.path.basename(path)
import glob
def find_files(pattern):
        return glob.glob(pattern)