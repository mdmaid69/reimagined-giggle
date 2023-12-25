  import os
  def get_file_name_without_extension(file_name):
        return os.path.splitext(file_name)[0]
import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread