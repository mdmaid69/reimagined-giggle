def calculate_present_value(future_value, rate, time):
        return future_value / (1 + rate)**time
import queue

q = queue.Queue()

for i in range(5):
        q.put(i)

while not q.empty():
        print(q.get())