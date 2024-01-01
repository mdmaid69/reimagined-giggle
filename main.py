  import os
  def get_file_blksize(file_name):
        return os.stat(file_name).st_blksize
import os
def get_environment_variable(var):
        return os.getenv(var)