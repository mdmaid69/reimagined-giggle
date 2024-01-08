import array
def get_string_from_array(array):
        return array.tobytes()
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("www.python.org", 80))