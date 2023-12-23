  import os
  def get_parent_directory(dir_name):
        return os.path.dirname(dir_name)
import threading

def print_hello():
        print("Hello, world!")

thread = threading.Thread(target=print_hello)
thread.start()
thread.join()