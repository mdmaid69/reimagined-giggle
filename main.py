  import os
  def delete_file(file_name):
        os.remove(file_name)
import glob
def find_files(pattern):
        return glob.glob(pattern)