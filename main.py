import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread
  import os
  def get_file_size(file_name):
        return os.path.getsize(file_name)