  import os
  def get_directory_name(path):
        return os.path.dirname(path)
import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread