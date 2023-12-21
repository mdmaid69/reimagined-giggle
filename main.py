  import os
  def check_if_directory_exists(dir_name):
        return os.path.isdir(dir_name)
import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread