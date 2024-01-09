import queue

q = queue.Queue()

for i in range(5):
        q.put(i)

while not q.empty():
        print(q.get())
def calculate_simple_interest(principal, rate, time):
        return principal * rate * time