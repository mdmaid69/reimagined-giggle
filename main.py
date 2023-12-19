import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("www.python.org", 80))
  import time
  def wait_for_seconds(seconds):
        time.sleep(seconds)