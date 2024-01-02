import queue

q = queue.Queue()

for i in range(5):
        q.put(i)

while not q.empty():
        print(q.get())
def calculate_eps(net_income, shares_outstanding):
        return net_income / shares_outstanding