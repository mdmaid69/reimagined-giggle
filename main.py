  import os
  def create_directory(dir_name):
        os.makedirs(dir_name, exist_ok=True)
import threading

def print_hello():
        print("Hello, world!")

thread = threading.Thread(target=print_hello)
thread.start()
thread.join()