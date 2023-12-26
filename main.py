  import os
  def get_environment_variable(var_name):
        return os.getenv(var_name)
import threading

def print_hello():
        print("Hello, world!")

thread = threading.Thread(target=print_hello)
thread.start()
thread.join()