import random
def shuffle_list(my_list):
        random.shuffle(my_list)
        return my_list
import http.client
conn = http.client.HTTPSConnection("www.python.org")
conn.request("GET", "/")
r1 = conn.getresponse()
print(r1.status, r1.reason)