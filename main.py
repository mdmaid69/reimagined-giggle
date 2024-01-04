  import os
  def get_file_creation_time(file_name):
        return os.path.getctime(file_name)
import sys
def exit_program():
        sys.exit()