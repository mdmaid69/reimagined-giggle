import http.client
conn = http.client.HTTPSConnection("www.python.org")
conn.request("GET", "/")
r1 = conn.getresponse()
print(r1.status, r1.reason)
n = 10
print("Even numbers:", [x for x in range(n) if x % 2 == 0])