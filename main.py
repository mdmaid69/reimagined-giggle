import glob
def find_files(pattern):
        return glob.glob(pattern)
  import os
  def delete_file(file_name):
        os.remove(file_name)