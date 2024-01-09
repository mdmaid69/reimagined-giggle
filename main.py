  import os
  def get_file_flags(file_name):
        return os.stat(file_name).st_flags
import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread