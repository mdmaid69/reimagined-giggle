  import os
  def get_file_blocks_allocated(file_name):
        return os.stat(file_name).st_blocks
import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread