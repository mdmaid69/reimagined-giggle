import array
def convert_array_to_bytes(array):
        return array.tobytes()
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("www.python.org", 80))