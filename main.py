import http.client
conn = http.client.HTTPSConnection("www.python.org")
conn.request("GET", "/")
r1 = conn.getresponse()
print(r1.status, r1.reason)
  def find_min(lst):
        return min(lst) if len(lst) != 0 else "List is empty"