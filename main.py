def calculate_return_on_equity(net_income, total_equity):
        return net_income / total_equity
import queue

q = queue.Queue()

for i in range(5):
        q.put(i)

while not q.empty():
        print(q.get())