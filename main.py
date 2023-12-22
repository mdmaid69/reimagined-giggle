import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread
  import os
  def list_files_in_directory(dir_name):
        return os.listdir(dir_name)