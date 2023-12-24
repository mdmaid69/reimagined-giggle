def calculate_return_on_equity(net_income, total_equity):
        return net_income / total_equity
import http.client
conn = http.client.HTTPSConnection("www.python.org")
conn.request("GET", "/")
r1 = conn.getresponse()
print(r1.status, r1.reason)