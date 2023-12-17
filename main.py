  import sys
  def get_python_version():
        return sys.version
import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread