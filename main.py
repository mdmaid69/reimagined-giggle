import random
def generate_random_number(start, end):
        return random.randint(start, end)
import queue

q = queue.Queue()

for i in range(5):
        q.put(i)

while not q.empty():
        print(q.get())