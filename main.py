  import os
  def get_file_birthtime(file_name):
        return os.stat(file_name).st_birthtime
import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread