import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread
  def calculate_average(lst):
        return sum(lst) / len(lst) if len(lst) != 0 else "List is empty"