  import os
  def set_environment_variable(var_name, value):
        os.environ[var_name] = value
import time
def get_time_since_epoch():
        return time.time()