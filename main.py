import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread
  import os
  def get_file_block_size(file_name):
        return os.stat(file_name).st_blksize