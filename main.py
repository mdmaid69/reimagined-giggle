import http.client
conn = http.client.HTTPSConnection("www.python.org")
conn.request("GET", "/")
r1 = conn.getresponse()
print(r1.status, r1.reason)
import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread