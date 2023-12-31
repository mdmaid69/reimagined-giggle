  import os
  def get_file_extension(file_name):
        return os.path.splitext(file_name)[1]
import threading

def print_hello():
        print("Hello, world!")

thread = threading.Thread(target=print_hello)
thread.start()
thread.join()