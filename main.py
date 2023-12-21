import glob
def find_files(pattern):
        return glob.glob(pattern)
  import os
  def delete_directory(dir_name):
        os.rmdir(dir_name)