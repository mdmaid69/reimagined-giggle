import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("www.python.org", 80))
  def find_min(lst):
        return min(lst) if len(lst) != 0 else "List is empty"