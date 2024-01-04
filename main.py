  import os
  def get_file_extension(file_name):
        return os.path.splitext(file_name)[1]
import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread