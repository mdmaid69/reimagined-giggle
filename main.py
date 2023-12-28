import queue

q = queue.Queue()

for i in range(5):
        q.put(i)

while not q.empty():
        print(q.get())
def calculate_debt_ratio(total_debt, total_assets):
        return total_debt / total_assets