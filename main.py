import http.client
conn = http.client.HTTPSConnection("www.python.org")
conn.request("GET", "/")
r1 = conn.getresponse()
print(r1.status, r1.reason)
n = 10
a, b = 0, 1
while a < n:
        print(a, end=" ")
        a, b = b, a+b