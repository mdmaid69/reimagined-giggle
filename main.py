import http.client
conn = http.client.HTTPSConnection("www.python.org")
conn.request("GET", "/")
r1 = conn.getresponse()
print(r1.status, r1.reason)
def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)