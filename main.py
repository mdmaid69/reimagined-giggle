def calculate_current_ratio(current_assets, current_liabilities):
        return current_assets / current_liabilities
import queue

q = queue.Queue()

for i in range(5):
        q.put(i)

while not q.empty():
        print(q.get())