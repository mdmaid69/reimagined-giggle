  import os
  def check_if_file_exists(file_name):
        return os.path.isfile(file_name)
import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread