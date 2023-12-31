  import os
  def join_paths(path1, path2):
        return os.path.join(path1, path2)
import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread