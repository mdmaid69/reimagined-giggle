  import os
  def get_base_name(path):
        return os.path.basename(path)
import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread