  import datetime
  def get_current_date():
        return datetime.datetime.now().date()
import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread