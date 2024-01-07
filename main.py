import array
def convert_array_to_list(array):
        return array.tolist()
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("www.python.org", 80))