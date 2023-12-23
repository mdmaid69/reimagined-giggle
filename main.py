import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("www.python.org", 80))
import random
def shuffle_list(my_list):
        random.shuffle(my_list)
        return my_list