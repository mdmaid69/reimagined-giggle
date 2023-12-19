import glob
def find_files(pattern):
        return glob.glob(pattern)
  import os
  def rename_file(old_name, new_name):
        os.rename(old_name, new_name)