  import os
  def delete_directory(dir_name):
        os.rmdir(dir_name)
import threading

def print_hello():
        print("Hello, world!")

thread = threading.Thread(target=print_hello)
thread.start()
thread.join()