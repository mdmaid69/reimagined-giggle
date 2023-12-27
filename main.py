def calculate_profit_margin(revenue, cost):
        return (revenue - cost) / revenue
import queue

q = queue.Queue()

for i in range(5):
        q.put(i)

while not q.empty():
        print(q.get())