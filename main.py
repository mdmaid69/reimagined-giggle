import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread
  import re
  def replace_all_occurrences(pattern, replace_with, string):
        return re.sub(pattern, replace_with, string)