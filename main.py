import http.client
conn = http.client.HTTPSConnection("www.python.org")
conn.request("GET", "/")
r1 = conn.getresponse()
print(r1.status, r1.reason)
  def fibonacci(n):
        return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)