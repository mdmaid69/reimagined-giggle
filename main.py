import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread
  import os
  def delete_directory(dir_name):
        os.rmdir(dir_name)