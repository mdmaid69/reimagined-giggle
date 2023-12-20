  import time
  def wait_for_seconds(seconds):
        time.sleep(seconds)
import os
def get_environment_variable(var):
        return os.getenv(var)