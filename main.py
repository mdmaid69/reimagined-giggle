import threading

def print_hello():
        print("Hello, world!")

thread = threading.Thread(target=print_hello)
thread.start()
thread.join()
  import re
  def find_all_occurrences(pattern, string):
        return re.findall(pattern, string)