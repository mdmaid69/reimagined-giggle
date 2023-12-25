  import time
  def wait_for_seconds(seconds):
        time.sleep(seconds)
  import os
  def set_environment_variable(var_name, value):
        os.environ[var_name] = value