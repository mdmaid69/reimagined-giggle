import threading

def print_hello():
        print("Hello, world!")

thread = threading.Thread(target=print_hello)
thread.start()
thread.join()
  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)