  import os
  def get_environment_variable(var_name):
        return os.getenv(var_name)
import shutil
def copy_file(src, dst):
        shutil.copy(src, dst)