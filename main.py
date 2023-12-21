import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread
  def reverse_list(lst):
        return lst[::-1]