  import os
  def get_file_creation_time(file_name):
        return os.path.getctime(file_name)
import threading

def print_hello():
        print("Hello, world!")

thread = threading.Thread(target=print_hello)
thread.start()
thread.join()