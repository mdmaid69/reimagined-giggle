  import os
  def get_file_qspare(file_name):
        return os.stat(file_name).st_qspare
  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)