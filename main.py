import http.client
conn = http.client.HTTPSConnection("www.python.org")
conn.request("GET", "/")
r1 = conn.getresponse()
print(r1.status, r1.reason)
  def divide_numbers(x, y):
        return x / y if y != 0 else "Cannot divide by zero"