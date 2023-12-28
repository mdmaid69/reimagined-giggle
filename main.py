def calculate_present_value(future_value, rate, time):
        return future_value / (1 + rate)**time
import http.client
conn = http.client.HTTPSConnection("www.python.org")
conn.request("GET", "/")
r1 = conn.getresponse()
print(r1.status, r1.reason)