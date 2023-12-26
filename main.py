  import os
  def get_environment_variable(var_name):
        return os.getenv(var_name)
import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread