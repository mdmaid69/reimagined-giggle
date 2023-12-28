import http.client
conn = http.client.HTTPSConnection("www.python.org")
conn.request("GET", "/")
r1 = conn.getresponse()
print(r1.status, r1.reason)
n = 10
print("Fibonacci:", [((1 + 5**0.5) / 2)**n / 5**0.5 for n in range(n)])