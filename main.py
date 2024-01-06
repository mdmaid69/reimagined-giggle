def calculate_pe_ratio(price_per_share, eps):
        return price_per_share / eps
import http.client
conn = http.client.HTTPSConnection("www.python.org")
conn.request("GET", "/")
r1 = conn.getresponse()
print(r1.status, r1.reason)