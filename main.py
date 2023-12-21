  def find_max(lst):
        return max(lst) if len(lst) != 0 else "List is empty"
import http.client
conn = http.client.HTTPSConnection("www.python.org")
conn.request("GET", "/")
r1 = conn.getresponse()
print(r1.status, r1.reason)