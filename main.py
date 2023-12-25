  import os
  def split_path(path):
        return os.path.split(path)
import threading

def print_hello():
        print("Hello, world!")

thread = threading.Thread(target=print_hello)
thread.start()
thread.join()