  import os
  def get_environment_variable(var_name):
        return os.getenv(var_name)
import time
def get_current_time():
        return time.ctime()