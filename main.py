numbers = [1, 2, 3, 4, 5]
print("Average:", sum(numbers) / len(numbers))
import http.client
conn = http.client.HTTPSConnection("www.python.org")
conn.request("GET", "/")
r1 = conn.getresponse()
print(r1.status, r1.reason)