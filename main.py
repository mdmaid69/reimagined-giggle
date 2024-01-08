import threading

def print_hello():
        print("Hello, world!")

thread = threading.Thread(target=print_hello)
thread.start()
thread.join()
  import os
  def delete_file(file_name):
        os.remove(file_name)