import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread
  def sort_list(lst):
        return sorted(lst)