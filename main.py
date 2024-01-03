import sys
def exit_program():
        sys.exit()
  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)