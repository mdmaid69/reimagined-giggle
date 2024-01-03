import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("www.python.org", 80))
def find_union(list1, list2):
        return set(list1) | set(list2)