def calculate_return_on_assets(net_income, total_assets):
        return net_income / total_assets
import queue

q = queue.Queue()

for i in range(5):
        q.put(i)

while not q.empty():
        print(q.get())