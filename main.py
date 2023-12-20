def calculate_eps(net_income, shares_outstanding):
        return net_income / shares_outstanding
import http.client
conn = http.client.HTTPSConnection("www.python.org")
conn.request("GET", "/")
r1 = conn.getresponse()
print(r1.status, r1.reason)