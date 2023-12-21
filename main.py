import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread
  import os
  def get_file_modification_time(file_name):
        return os.path.getmtime(file_name)