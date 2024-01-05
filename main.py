import threading

def print_hello():
        print("Hello, world!")

thread = threading.Thread(target=print_hello)
thread.start()
thread.join()
  import os
  def get_absolute_path(file_name):
        return os.path.abspath(file_name)