import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread
  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)