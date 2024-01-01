  import os
  def get_file_creation_time(file_name):
        return os.path.getctime(file_name)
import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread