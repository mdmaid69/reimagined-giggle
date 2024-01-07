  import os
  def join_paths(path1, path2):
        return os.path.join(path1, path2)
import threading

def print_hello():
        print("Hello, world!")

thread = threading.Thread(target=print_hello)
thread.start()
thread.join()