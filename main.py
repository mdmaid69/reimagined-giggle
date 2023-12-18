import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("www.python.org", 80))
  import os
  def delete_file(file_name):
        os.remove(file_name)