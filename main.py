  import os
  def get_file_blocks(file_name):
        return os.stat(file_name).st_blocks
import sys
def exit_program():
        sys.exit()