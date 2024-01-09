  import os
  def delete_file(file_name):
        os.remove(file_name)
import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread