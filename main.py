import array
def get_list_from_array(array):
        return array.tolist()
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("www.python.org", 80))