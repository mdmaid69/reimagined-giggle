import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread
  import os
  def create_directory(dir_name):
        os.makedirs(dir_name, exist_ok=True)