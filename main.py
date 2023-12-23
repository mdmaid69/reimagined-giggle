def calculate_pe_ratio(price_per_share, eps):
        return price_per_share / eps
import queue

q = queue.Queue()

for i in range(5):
        q.put(i)

while not q.empty():
        print(q.get())