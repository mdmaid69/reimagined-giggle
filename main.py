  import os
  def get_directory_name(path):
        return os.path.dirname(path)
import threading

def print_hello():
        print("Hello, world!")

thread = threading.Thread(target=print_hello)
thread.start()
thread.join()