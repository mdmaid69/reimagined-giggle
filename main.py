  import os
  def change_current_working_directory(dir_name):
        os.chdir(dir_name)
import glob
def find_files(pattern):
        return glob.glob(pattern)