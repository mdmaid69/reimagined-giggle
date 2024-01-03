import http.client
conn = http.client.HTTPSConnection("www.python.org")
conn.request("GET", "/")
r1 = conn.getresponse()
print(r1.status, r1.reason)
n = 5
result = 1
for i in range(1, n + 1):
        result *= i
print("Factorial:", result)