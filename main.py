import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("www.python.org", 80))
import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)