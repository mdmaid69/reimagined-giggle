import threading

def print_hello():
        print("Hello, world!")

thread = threading.Thread(target=print_hello)
thread.start()
thread.join()
  import os
  def change_current_working_directory(dir_name):
        os.chdir(dir_name)