  import os
  def get_current_directory():
        return os.getcwd()
import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread