  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)
  def cube_number(x):
        return x**3