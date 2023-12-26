  import os
  def list_files_in_directory(dir_name):
        return os.listdir(dir_name)
import threading

def print_hello():
        print("Hello, world!")

thread = threading.Thread(target=print_hello)
thread.start()
thread.join()