def find_difference(list1, list2):
        return set(list1) - set(list2)
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("www.python.org", 80))