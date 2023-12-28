import random
def flip_coin():
        return "Heads" if random.random() < 0.5 else "Tails"
import http.client
conn = http.client.HTTPSConnection("www.python.org")
conn.request("GET", "/")
r1 = conn.getresponse()
print(r1.status, r1.reason)