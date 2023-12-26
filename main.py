import array
def get_array_buffer_info(array):
        return array.buffer_info()
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("www.python.org", 80))