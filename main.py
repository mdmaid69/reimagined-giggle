  import os
  def get_parent_directory(dir_name):
        return os.path.dirname(dir_name)
import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread