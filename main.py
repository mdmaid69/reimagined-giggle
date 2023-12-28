  import os
  def get_file_size(file_name):
        return os.stat(file_name).st_size
import threading

def print_hello():
        print("Hello, world!")

thread = threading.Thread(target=print_hello)
thread.start()
thread.join()