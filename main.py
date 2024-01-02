  import os
  def get_file_modification_time(file_name):
        return os.path.getmtime(file_name)
import threading

def print_hello():
        print("Hello, world!")

thread = threading.Thread(target=print_hello)
thread.start()
thread.join()