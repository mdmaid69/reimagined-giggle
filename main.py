  import os
  def rename_file(old_name, new_name):
        os.rename(old_name, new_name)
import threading

def print_hello():
        print("Hello, world!")

thread = threading.Thread(target=print_hello)
thread.start()
thread.join()