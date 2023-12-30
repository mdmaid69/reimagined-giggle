  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)
import glob
def find_files(pattern):
        return glob.glob(pattern)