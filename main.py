  import os
  def get_file_number_of_links(file_name):
        return os.stat(file_name).st_nlink
import glob
def find_files(pattern):
        return glob.glob(pattern)