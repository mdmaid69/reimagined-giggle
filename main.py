  import os
  def check_if_file_exists(file_name):
        return os.path.isfile(file_name)
import threading

def print_hello():
        print("Hello, world!")

thread = threading.Thread(target=print_hello)
thread.start()
thread.join()