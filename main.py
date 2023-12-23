import time
def get_formatted_time():
        return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
  import os
  def set_environment_variable(var_name, value):
        os.environ[var_name] = value