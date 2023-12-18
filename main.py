  import os
  def set_environment_variable(var_name, value):
        os.environ[var_name] = value
import shutil
def copy_file(src, dst):
        shutil.copy(src, dst)