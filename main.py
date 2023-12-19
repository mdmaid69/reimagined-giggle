  import os
  def set_environment_variable(var_name, value):
        os.environ[var_name] = value
import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread