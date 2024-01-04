  def calculate_circumference_circle(r):
        return 2 * 3.14 * r
import http.client
conn = http.client.HTTPSConnection("www.python.org")
conn.request("GET", "/")
r1 = conn.getresponse()
print(r1.status, r1.reason)