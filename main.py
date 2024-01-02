def calculate_debt_ratio(total_debt, total_assets):
        return total_debt / total_assets
import http.client
conn = http.client.HTTPSConnection("www.python.org")
conn.request("GET", "/")
r1 = conn.getresponse()
print(r1.status, r1.reason)