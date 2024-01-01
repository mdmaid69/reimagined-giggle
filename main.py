  import os
  def check_if_directory_exists(dir_name):
        return os.path.isdir(dir_name)
import threading

def print_hello():
        print("Hello, world!")

thread = threading.Thread(target=print_hello)
thread.start()
thread.join()