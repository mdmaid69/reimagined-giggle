  import os
  def set_environment_variable(var_name, value):
        os.environ[var_name] = value
import time
def get_current_time():
        return time.ctime()