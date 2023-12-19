import http.client
conn = http.client.HTTPSConnection("www.python.org")
conn.request("GET", "/")
r1 = conn.getresponse()
print(r1.status, r1.reason)
def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)