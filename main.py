  import os
  def get_file_blksize(file_name):
        return os.stat(file_name).st_blksize
  import os
  def set_environment_variable(var_name, value):
        os.environ[var_name] = value