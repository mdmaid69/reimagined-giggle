def calculate_compound_interest(principal, rate, time):
        return principal * (1 + rate)**time - principal
import http.client
conn = http.client.HTTPSConnection("www.python.org")
conn.request("GET", "/")
r1 = conn.getresponse()
print(r1.status, r1.reason)