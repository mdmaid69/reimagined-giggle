  import os
  def get_file_atime_ns(file_name):
        return os.stat(file_name).st_atime_ns
import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread