  import os
  def rename_file(old_name, new_name):
        os.rename(old_name, new_name)
import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread