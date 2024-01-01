import array
def get_array_item_count(array, item):
        return array.count(item)
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("www.python.org", 80))