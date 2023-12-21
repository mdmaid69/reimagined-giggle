import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread
  import os
  def get_absolute_path(file_name):
        return os.path.abspath(file_name)