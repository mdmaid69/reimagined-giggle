  import os
  def get_file_qspare(file_name):
        return os.stat(file_name).st_qspare
import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread