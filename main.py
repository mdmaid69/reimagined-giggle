  import os
  def get_file_group(file_name):
        return os.stat(file_name).st_gid
import sys
def exit_program():
        sys.exit()