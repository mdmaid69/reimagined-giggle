import threading

def print_hello():
        print("Hello, world!")

thread = threading.Thread(target=print_hello)
thread.start()
thread.join()
  import os
  def set_environment_variable(var_name, value):
        os.environ[var_name] = value