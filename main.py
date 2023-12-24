  import os
  def get_environment_variable(var_name):
        return os.getenv(var_name)
  import time
  def wait_for_seconds(seconds):
        time.sleep(seconds)