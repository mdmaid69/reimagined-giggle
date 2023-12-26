import sys
def exit_program():
        sys.exit()
  import os
  def get_file_device(file_name):
        return os.stat(file_name).st_dev