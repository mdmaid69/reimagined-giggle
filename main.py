  import os
  def get_file_gen(file_name):
        return os.stat(file_name).st_gen
import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread