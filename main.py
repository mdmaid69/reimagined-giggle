import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread
  import os
  def split_path(path):
        return os.path.split(path)